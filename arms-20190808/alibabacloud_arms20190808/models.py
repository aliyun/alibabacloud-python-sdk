# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class AddASMIntegrationRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddASMIntegrationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        state: bool = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class AddASMIntegrationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddASMIntegrationResponseBody = None,
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
            temp_model = AddASMIntegrationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddAliClusterIdsToPrometheusGlobalViewRequest(TeaModel):
    def __init__(
        self,
        cluster_ids: str = None,
        global_view_cluster_id: str = None,
        group_name: str = None,
        region_id: str = None,
    ):
        self.cluster_ids = cluster_ids
        self.global_view_cluster_id = global_view_cluster_id
        self.group_name = group_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_ids is not None:
            result['ClusterIds'] = self.cluster_ids
        if self.global_view_cluster_id is not None:
            result['GlobalViewClusterId'] = self.global_view_cluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterIds') is not None:
            self.cluster_ids = m.get('ClusterIds')
        if m.get('GlobalViewClusterId') is not None:
            self.global_view_cluster_id = m.get('GlobalViewClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddAliClusterIdsToPrometheusGlobalViewResponseBodyData(TeaModel):
    def __init__(
        self,
        info: str = None,
        msg: str = None,
        success: bool = None,
    ):
        self.info = info
        self.msg = msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info is not None:
            result['Info'] = self.info
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Info') is not None:
            self.info = m.get('Info')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddAliClusterIdsToPrometheusGlobalViewResponseBody(TeaModel):
    def __init__(
        self,
        data: AddAliClusterIdsToPrometheusGlobalViewResponseBodyData = None,
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
            temp_model = AddAliClusterIdsToPrometheusGlobalViewResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddAliClusterIdsToPrometheusGlobalViewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddAliClusterIdsToPrometheusGlobalViewResponseBody = None,
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
            temp_model = AddAliClusterIdsToPrometheusGlobalViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddGrafanaRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        integration: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.integration = integration
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.integration is not None:
            result['Integration'] = self.integration
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Integration') is not None:
            self.integration = m.get('Integration')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddGrafanaResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
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


class AddGrafanaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddGrafanaResponseBody = None,
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
            temp_model = AddGrafanaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddIntegrationRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        integration: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.integration = integration
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.integration is not None:
            result['Integration'] = self.integration
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Integration') is not None:
            self.integration = m.get('Integration')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddIntegrationResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
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


class AddIntegrationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddIntegrationResponseBody = None,
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
            temp_model = AddIntegrationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddPrometheusGlobalViewRequest(TeaModel):
    def __init__(
        self,
        clusters: str = None,
        group_name: str = None,
        region_id: str = None,
    ):
        self.clusters = clusters
        self.group_name = group_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clusters is not None:
            result['Clusters'] = self.clusters
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clusters') is not None:
            self.clusters = m.get('Clusters')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddPrometheusGlobalViewResponseBodyData(TeaModel):
    def __init__(
        self,
        info: str = None,
        msg: str = None,
        success: bool = None,
    ):
        self.info = info
        self.msg = msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info is not None:
            result['Info'] = self.info
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Info') is not None:
            self.info = m.get('Info')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddPrometheusGlobalViewResponseBody(TeaModel):
    def __init__(
        self,
        data: AddPrometheusGlobalViewResponseBodyData = None,
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
            temp_model = AddPrometheusGlobalViewResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddPrometheusGlobalViewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddPrometheusGlobalViewResponseBody = None,
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
            temp_model = AddPrometheusGlobalViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddPrometheusGlobalViewByAliClusterIdsRequest(TeaModel):
    def __init__(
        self,
        cluster_ids: str = None,
        group_name: str = None,
        product_code: str = None,
        region_id: str = None,
    ):
        self.cluster_ids = cluster_ids
        self.group_name = group_name
        self.product_code = product_code
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_ids is not None:
            result['ClusterIds'] = self.cluster_ids
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterIds') is not None:
            self.cluster_ids = m.get('ClusterIds')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddPrometheusGlobalViewByAliClusterIdsResponseBodyData(TeaModel):
    def __init__(
        self,
        info: str = None,
        msg: str = None,
        success: bool = None,
    ):
        self.info = info
        self.msg = msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info is not None:
            result['Info'] = self.info
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Info') is not None:
            self.info = m.get('Info')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddPrometheusGlobalViewByAliClusterIdsResponseBody(TeaModel):
    def __init__(
        self,
        data: AddPrometheusGlobalViewByAliClusterIdsResponseBodyData = None,
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
            temp_model = AddPrometheusGlobalViewByAliClusterIdsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddPrometheusGlobalViewByAliClusterIdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddPrometheusGlobalViewByAliClusterIdsResponseBody = None,
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
            temp_model = AddPrometheusGlobalViewByAliClusterIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddRecordingRuleRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
        rule_yaml: str = None,
    ):
        self.cluster_id = cluster_id
        self.region_id = region_id
        self.rule_yaml = rule_yaml

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_yaml is not None:
            result['RuleYaml'] = self.rule_yaml
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleYaml') is not None:
            self.rule_yaml = m.get('RuleYaml')
        return self


class AddRecordingRuleResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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


class AddRecordingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddRecordingRuleResponseBody = None,
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
            temp_model = AddRecordingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppendInstancesToPrometheusGlobalViewRequest(TeaModel):
    def __init__(
        self,
        clusters: str = None,
        global_view_cluster_id: str = None,
        group_name: str = None,
        region_id: str = None,
    ):
        self.clusters = clusters
        self.global_view_cluster_id = global_view_cluster_id
        self.group_name = group_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clusters is not None:
            result['Clusters'] = self.clusters
        if self.global_view_cluster_id is not None:
            result['GlobalViewClusterId'] = self.global_view_cluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clusters') is not None:
            self.clusters = m.get('Clusters')
        if m.get('GlobalViewClusterId') is not None:
            self.global_view_cluster_id = m.get('GlobalViewClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AppendInstancesToPrometheusGlobalViewResponseBodyData(TeaModel):
    def __init__(
        self,
        info: str = None,
        msg: str = None,
        success: bool = None,
    ):
        self.info = info
        self.msg = msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info is not None:
            result['Info'] = self.info
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Info') is not None:
            self.info = m.get('Info')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AppendInstancesToPrometheusGlobalViewResponseBody(TeaModel):
    def __init__(
        self,
        data: AppendInstancesToPrometheusGlobalViewResponseBodyData = None,
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
            temp_model = AppendInstancesToPrometheusGlobalViewResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AppendInstancesToPrometheusGlobalViewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AppendInstancesToPrometheusGlobalViewResponseBody = None,
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
            temp_model = AppendInstancesToPrometheusGlobalViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyScenarioRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        config: Dict[str, Any] = None,
        name: str = None,
        region_id: str = None,
        scenario: str = None,
        sign: str = None,
        sn_dump: bool = None,
        sn_force: bool = None,
        sn_stat: bool = None,
        sn_transfer: bool = None,
        update_option: bool = None,
    ):
        self.app_id = app_id
        self.config = config
        self.name = name
        self.region_id = region_id
        self.scenario = scenario
        self.sign = sign
        self.sn_dump = sn_dump
        self.sn_force = sn_force
        self.sn_stat = sn_stat
        self.sn_transfer = sn_transfer
        self.update_option = update_option

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.config is not None:
            result['Config'] = self.config
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scenario is not None:
            result['Scenario'] = self.scenario
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.sn_dump is not None:
            result['SnDump'] = self.sn_dump
        if self.sn_force is not None:
            result['SnForce'] = self.sn_force
        if self.sn_stat is not None:
            result['SnStat'] = self.sn_stat
        if self.sn_transfer is not None:
            result['SnTransfer'] = self.sn_transfer
        if self.update_option is not None:
            result['UpdateOption'] = self.update_option
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('SnDump') is not None:
            self.sn_dump = m.get('SnDump')
        if m.get('SnForce') is not None:
            self.sn_force = m.get('SnForce')
        if m.get('SnStat') is not None:
            self.sn_stat = m.get('SnStat')
        if m.get('SnTransfer') is not None:
            self.sn_transfer = m.get('SnTransfer')
        if m.get('UpdateOption') is not None:
            self.update_option = m.get('UpdateOption')
        return self


class ApplyScenarioShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        config_shrink: str = None,
        name: str = None,
        region_id: str = None,
        scenario: str = None,
        sign: str = None,
        sn_dump: bool = None,
        sn_force: bool = None,
        sn_stat: bool = None,
        sn_transfer: bool = None,
        update_option: bool = None,
    ):
        self.app_id = app_id
        self.config_shrink = config_shrink
        self.name = name
        self.region_id = region_id
        self.scenario = scenario
        self.sign = sign
        self.sn_dump = sn_dump
        self.sn_force = sn_force
        self.sn_stat = sn_stat
        self.sn_transfer = sn_transfer
        self.update_option = update_option

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.config_shrink is not None:
            result['Config'] = self.config_shrink
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scenario is not None:
            result['Scenario'] = self.scenario
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.sn_dump is not None:
            result['SnDump'] = self.sn_dump
        if self.sn_force is not None:
            result['SnForce'] = self.sn_force
        if self.sn_stat is not None:
            result['SnStat'] = self.sn_stat
        if self.sn_transfer is not None:
            result['SnTransfer'] = self.sn_transfer
        if self.update_option is not None:
            result['UpdateOption'] = self.update_option
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Config') is not None:
            self.config_shrink = m.get('Config')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('SnDump') is not None:
            self.sn_dump = m.get('SnDump')
        if m.get('SnForce') is not None:
            self.sn_force = m.get('SnForce')
        if m.get('SnStat') is not None:
            self.sn_stat = m.get('SnStat')
        if m.get('SnTransfer') is not None:
            self.sn_transfer = m.get('SnTransfer')
        if m.get('UpdateOption') is not None:
            self.update_option = m.get('UpdateOption')
        return self


class ApplyScenarioResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ApplyScenarioResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyScenarioResponseBody = None,
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
            temp_model = ApplyScenarioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CMonitorAlertEventRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        kind: str = None,
        name: str = None,
        namespace: str = None,
        page: str = None,
        page_size: str = None,
        proxy_user_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.kind = kind
        self.name = name
        self.namespace = namespace
        self.page = page
        self.page_size = page_size
        self.proxy_user_id = proxy_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.kind is not None:
            result['Kind'] = self.kind
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        return self


class CMonitorAlertEventResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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


class CMonitorAlertEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CMonitorAlertEventResponseBody = None,
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
            temp_model = CMonitorAlertEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckServiceStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        svc_code: str = None,
    ):
        self.region_id = region_id
        self.svc_code = svc_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.svc_code is not None:
            result['SvcCode'] = self.svc_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SvcCode') is not None:
            self.svc_code = m.get('SvcCode')
        return self


class CheckServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
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


class CheckServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckServiceStatusResponseBody = None,
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
            temp_model = CheckServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigAppRequest(TeaModel):
    def __init__(
        self,
        app_ids: str = None,
        enable: str = None,
        region_id: str = None,
    ):
        self.app_ids = app_ids
        self.enable = enable
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ConfigAppResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
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


class ConfigAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigAppResponseBody = None,
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
            temp_model = ConfigAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAlertContactRequest(TeaModel):
    def __init__(
        self,
        contact_name: str = None,
        ding_robot_webhook_url: str = None,
        email: str = None,
        phone_num: str = None,
        region_id: str = None,
        system_noc: bool = None,
    ):
        self.contact_name = contact_name
        self.ding_robot_webhook_url = ding_robot_webhook_url
        self.email = email
        self.phone_num = phone_num
        self.region_id = region_id
        self.system_noc = system_noc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.ding_robot_webhook_url is not None:
            result['DingRobotWebhookUrl'] = self.ding_robot_webhook_url
        if self.email is not None:
            result['Email'] = self.email
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.system_noc is not None:
            result['SystemNoc'] = self.system_noc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('DingRobotWebhookUrl') is not None:
            self.ding_robot_webhook_url = m.get('DingRobotWebhookUrl')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SystemNoc') is not None:
            self.system_noc = m.get('SystemNoc')
        return self


class CreateAlertContactResponseBody(TeaModel):
    def __init__(
        self,
        contact_id: str = None,
        request_id: str = None,
    ):
        self.contact_id = contact_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAlertContactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAlertContactResponseBody = None,
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
            temp_model = CreateAlertContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAlertContactGroupRequest(TeaModel):
    def __init__(
        self,
        contact_group_name: str = None,
        contact_ids: str = None,
        region_id: str = None,
    ):
        self.contact_group_name = contact_group_name
        self.contact_ids = contact_ids
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateAlertContactGroupResponseBody(TeaModel):
    def __init__(
        self,
        contact_group_id: str = None,
        request_id: str = None,
    ):
        self.contact_group_id = contact_group_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAlertContactGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAlertContactGroupResponseBody = None,
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
            temp_model = CreateAlertContactGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDispatchRuleRequest(TeaModel):
    def __init__(
        self,
        dispatch_rule: str = None,
        region_id: str = None,
    ):
        self.dispatch_rule = dispatch_rule
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dispatch_rule is not None:
            result['DispatchRule'] = self.dispatch_rule
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DispatchRule') is not None:
            self.dispatch_rule = m.get('DispatchRule')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateDispatchRuleResponseBody(TeaModel):
    def __init__(
        self,
        dispatch_rule_id: int = None,
        request_id: str = None,
    ):
        self.dispatch_rule_id = dispatch_rule_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDispatchRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDispatchRuleResponseBody = None,
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
            temp_model = CreateDispatchRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrUpdateAlertRuleRequest(TeaModel):
    def __init__(
        self,
        alert_check_type: str = None,
        alert_group: int = None,
        alert_id: int = None,
        alert_name: str = None,
        alert_rule_content: str = None,
        alert_status: str = None,
        alert_type: str = None,
        annotations: str = None,
        auto_add_new_application: bool = None,
        cluster_id: str = None,
        duration: int = None,
        filters: str = None,
        labels: str = None,
        level: str = None,
        message: str = None,
        metrics_key: str = None,
        metrics_type: str = None,
        notify_strategy: str = None,
        pids: str = None,
        prom_ql: str = None,
        region_id: str = None,
    ):
        self.alert_check_type = alert_check_type
        self.alert_group = alert_group
        # 告警规则ID
        self.alert_id = alert_id
        # 告警规则名称
        self.alert_name = alert_name
        self.alert_rule_content = alert_rule_content
        self.alert_status = alert_status
        # 告警规则类型
        self.alert_type = alert_type
        self.annotations = annotations
        self.auto_add_new_application = auto_add_new_application
        self.cluster_id = cluster_id
        self.duration = duration
        self.filters = filters
        self.labels = labels
        self.level = level
        self.message = message
        self.metrics_key = metrics_key
        self.metrics_type = metrics_type
        self.notify_strategy = notify_strategy
        self.pids = pids
        self.prom_ql = prom_ql
        # 地域
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_check_type is not None:
            result['AlertCheckType'] = self.alert_check_type
        if self.alert_group is not None:
            result['AlertGroup'] = self.alert_group
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_rule_content is not None:
            result['AlertRuleContent'] = self.alert_rule_content
        if self.alert_status is not None:
            result['AlertStatus'] = self.alert_status
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.annotations is not None:
            result['Annotations'] = self.annotations
        if self.auto_add_new_application is not None:
            result['AutoAddNewApplication'] = self.auto_add_new_application
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.filters is not None:
            result['Filters'] = self.filters
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.metrics_key is not None:
            result['MetricsKey'] = self.metrics_key
        if self.metrics_type is not None:
            result['MetricsType'] = self.metrics_type
        if self.notify_strategy is not None:
            result['NotifyStrategy'] = self.notify_strategy
        if self.pids is not None:
            result['Pids'] = self.pids
        if self.prom_ql is not None:
            result['PromQL'] = self.prom_ql
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertCheckType') is not None:
            self.alert_check_type = m.get('AlertCheckType')
        if m.get('AlertGroup') is not None:
            self.alert_group = m.get('AlertGroup')
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertRuleContent') is not None:
            self.alert_rule_content = m.get('AlertRuleContent')
        if m.get('AlertStatus') is not None:
            self.alert_status = m.get('AlertStatus')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')
        if m.get('AutoAddNewApplication') is not None:
            self.auto_add_new_application = m.get('AutoAddNewApplication')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Filters') is not None:
            self.filters = m.get('Filters')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MetricsKey') is not None:
            self.metrics_key = m.get('MetricsKey')
        if m.get('MetricsType') is not None:
            self.metrics_type = m.get('MetricsType')
        if m.get('NotifyStrategy') is not None:
            self.notify_strategy = m.get('NotifyStrategy')
        if m.get('Pids') is not None:
            self.pids = m.get('Pids')
        if m.get('PromQL') is not None:
            self.prom_ql = m.get('PromQL')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateOrUpdateAlertRuleResponseBodyAlertRuleAlertRuleContentAlertRuleItems(TeaModel):
    def __init__(
        self,
        aggregate: str = None,
        metric_key: str = None,
        n: float = None,
        operator: str = None,
        value: str = None,
    ):
        # 应用监控/前端监控-聚合方式
        self.aggregate = aggregate
        # 应用监控/前端监控-具体告警条件的指标
        self.metric_key = metric_key
        # 应用监控/前端监控-最近N分钟
        self.n = n
        # 应用监控/前端监控-判断条件
        self.operator = operator
        # 应用监控/前端监控-阈值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregate is not None:
            result['Aggregate'] = self.aggregate
        if self.metric_key is not None:
            result['MetricKey'] = self.metric_key
        if self.n is not None:
            result['N'] = self.n
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aggregate') is not None:
            self.aggregate = m.get('Aggregate')
        if m.get('MetricKey') is not None:
            self.metric_key = m.get('MetricKey')
        if m.get('N') is not None:
            self.n = m.get('N')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateOrUpdateAlertRuleResponseBodyAlertRuleAlertRuleContent(TeaModel):
    def __init__(
        self,
        alert_rule_items: List[CreateOrUpdateAlertRuleResponseBodyAlertRuleAlertRuleContentAlertRuleItems] = None,
        condition: str = None,
    ):
        # 应用监控/前端监控-告警条件
        self.alert_rule_items = alert_rule_items
        # 应用监控/前端监控-多个告警条件触发逻辑
        self.condition = condition

    def validate(self):
        if self.alert_rule_items:
            for k in self.alert_rule_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlertRuleItems'] = []
        if self.alert_rule_items is not None:
            for k in self.alert_rule_items:
                result['AlertRuleItems'].append(k.to_map() if k else None)
        if self.condition is not None:
            result['Condition'] = self.condition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_rule_items = []
        if m.get('AlertRuleItems') is not None:
            for k in m.get('AlertRuleItems'):
                temp_model = CreateOrUpdateAlertRuleResponseBodyAlertRuleAlertRuleContentAlertRuleItems()
                self.alert_rule_items.append(temp_model.from_map(k))
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')
        return self


class CreateOrUpdateAlertRuleResponseBodyAlertRuleAnnotations(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # 键
        self.name = name
        # 值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateOrUpdateAlertRuleResponseBodyAlertRuleFiltersCustomSLSFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        opt: str = None,
        show: bool = None,
        t: str = None,
        value: str = None,
    ):
        self.key = key
        self.opt = opt
        self.show = show
        self.t = t
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
        if self.opt is not None:
            result['Opt'] = self.opt
        if self.show is not None:
            result['Show'] = self.show
        if self.t is not None:
            result['T'] = self.t
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Opt') is not None:
            self.opt = m.get('Opt')
        if m.get('Show') is not None:
            self.show = m.get('Show')
        if m.get('T') is not None:
            self.t = m.get('T')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateOrUpdateAlertRuleResponseBodyAlertRuleFiltersDimFilters(TeaModel):
    def __init__(
        self,
        filter_key: str = None,
        filter_opt: str = None,
        filter_values: List[str] = None,
    ):
        self.filter_key = filter_key
        self.filter_opt = filter_opt
        self.filter_values = filter_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key
        if self.filter_opt is not None:
            result['FilterOpt'] = self.filter_opt
        if self.filter_values is not None:
            result['FilterValues'] = self.filter_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')
        if m.get('FilterOpt') is not None:
            self.filter_opt = m.get('FilterOpt')
        if m.get('FilterValues') is not None:
            self.filter_values = m.get('FilterValues')
        return self


class CreateOrUpdateAlertRuleResponseBodyAlertRuleFilters(TeaModel):
    def __init__(
        self,
        custom_slsfilters: List[CreateOrUpdateAlertRuleResponseBodyAlertRuleFiltersCustomSLSFilters] = None,
        custom_slsgroup_by_dimensions: List[str] = None,
        custom_slswheres: List[str] = None,
        dim_filters: List[CreateOrUpdateAlertRuleResponseBodyAlertRuleFiltersDimFilters] = None,
    ):
        self.custom_slsfilters = custom_slsfilters
        self.custom_slsgroup_by_dimensions = custom_slsgroup_by_dimensions
        self.custom_slswheres = custom_slswheres
        self.dim_filters = dim_filters

    def validate(self):
        if self.custom_slsfilters:
            for k in self.custom_slsfilters:
                if k:
                    k.validate()
        if self.dim_filters:
            for k in self.dim_filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomSLSFilters'] = []
        if self.custom_slsfilters is not None:
            for k in self.custom_slsfilters:
                result['CustomSLSFilters'].append(k.to_map() if k else None)
        if self.custom_slsgroup_by_dimensions is not None:
            result['CustomSLSGroupByDimensions'] = self.custom_slsgroup_by_dimensions
        if self.custom_slswheres is not None:
            result['CustomSLSWheres'] = self.custom_slswheres
        result['DimFilters'] = []
        if self.dim_filters is not None:
            for k in self.dim_filters:
                result['DimFilters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_slsfilters = []
        if m.get('CustomSLSFilters') is not None:
            for k in m.get('CustomSLSFilters'):
                temp_model = CreateOrUpdateAlertRuleResponseBodyAlertRuleFiltersCustomSLSFilters()
                self.custom_slsfilters.append(temp_model.from_map(k))
        if m.get('CustomSLSGroupByDimensions') is not None:
            self.custom_slsgroup_by_dimensions = m.get('CustomSLSGroupByDimensions')
        if m.get('CustomSLSWheres') is not None:
            self.custom_slswheres = m.get('CustomSLSWheres')
        self.dim_filters = []
        if m.get('DimFilters') is not None:
            for k in m.get('DimFilters'):
                temp_model = CreateOrUpdateAlertRuleResponseBodyAlertRuleFiltersDimFilters()
                self.dim_filters.append(temp_model.from_map(k))
        return self


class CreateOrUpdateAlertRuleResponseBodyAlertRuleLabels(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # 键
        self.name = name
        # 值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateOrUpdateAlertRuleResponseBodyAlertRule(TeaModel):
    def __init__(
        self,
        alert_check_type: str = None,
        alert_group: int = None,
        alert_id: float = None,
        alert_name: str = None,
        alert_rule_content: CreateOrUpdateAlertRuleResponseBodyAlertRuleAlertRuleContent = None,
        alert_status: str = None,
        alert_type: str = None,
        annotations: List[CreateOrUpdateAlertRuleResponseBodyAlertRuleAnnotations] = None,
        auto_add_new_application: bool = None,
        cluster_id: str = None,
        created_time: int = None,
        duration: str = None,
        extend: str = None,
        filters: CreateOrUpdateAlertRuleResponseBodyAlertRuleFilters = None,
        labels: List[CreateOrUpdateAlertRuleResponseBodyAlertRuleLabels] = None,
        level: str = None,
        message: str = None,
        metrics_type: str = None,
        notify_strategy: str = None,
        pids: List[str] = None,
        prom_ql: str = None,
        region_id: str = None,
        updated_time: int = None,
        user_id: str = None,
    ):
        # Prometheus告警-告警检查类型
        self.alert_check_type = alert_check_type
        # Prometheus告警-告警分组ID
        self.alert_group = alert_group
        # 告警规则ID
        self.alert_id = alert_id
        # 告警规则名称
        self.alert_name = alert_name
        # 应用监控/前端监控-告警规则内容
        self.alert_rule_content = alert_rule_content
        # 告警规则状态
        self.alert_status = alert_status
        # 告警规则类型
        self.alert_type = alert_type
        # Prometheus告警-Annotation
        self.annotations = annotations
        # 应用监控/前端监控-是否开启新创建应用追加到此告警规则
        self.auto_add_new_application = auto_add_new_application
        # Prometheus告警-集群ID
        self.cluster_id = cluster_id
        # 创建时间
        self.created_time = created_time
        # Prometheus告警-持续时间
        self.duration = duration
        # 扩展字段
        self.extend = extend
        # 应用监控/前端监控-告警条件-过滤项
        self.filters = filters
        # Prometheus告警-Label
        self.labels = labels
        # Prometheus告警-等级
        self.level = level
        # Prometheus告警-告警内容
        self.message = message
        # 应用监控/前端监控-告警指标类型
        self.metrics_type = metrics_type
        # 通知策略ID
        self.notify_strategy = notify_strategy
        # 应用监控/前端监控-告警关联应用ID
        self.pids = pids
        # Prometheus告警-PromQL语句
        self.prom_ql = prom_ql
        # 地域
        self.region_id = region_id
        # 更新时间
        self.updated_time = updated_time
        # 用户UID
        self.user_id = user_id

    def validate(self):
        if self.alert_rule_content:
            self.alert_rule_content.validate()
        if self.annotations:
            for k in self.annotations:
                if k:
                    k.validate()
        if self.filters:
            self.filters.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_check_type is not None:
            result['AlertCheckType'] = self.alert_check_type
        if self.alert_group is not None:
            result['AlertGroup'] = self.alert_group
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_rule_content is not None:
            result['AlertRuleContent'] = self.alert_rule_content.to_map()
        if self.alert_status is not None:
            result['AlertStatus'] = self.alert_status
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        result['Annotations'] = []
        if self.annotations is not None:
            for k in self.annotations:
                result['Annotations'].append(k.to_map() if k else None)
        if self.auto_add_new_application is not None:
            result['AutoAddNewApplication'] = self.auto_add_new_application
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.extend is not None:
            result['Extend'] = self.extend
        if self.filters is not None:
            result['Filters'] = self.filters.to_map()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.metrics_type is not None:
            result['MetricsType'] = self.metrics_type
        if self.notify_strategy is not None:
            result['NotifyStrategy'] = self.notify_strategy
        if self.pids is not None:
            result['Pids'] = self.pids
        if self.prom_ql is not None:
            result['PromQL'] = self.prom_ql
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertCheckType') is not None:
            self.alert_check_type = m.get('AlertCheckType')
        if m.get('AlertGroup') is not None:
            self.alert_group = m.get('AlertGroup')
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertRuleContent') is not None:
            temp_model = CreateOrUpdateAlertRuleResponseBodyAlertRuleAlertRuleContent()
            self.alert_rule_content = temp_model.from_map(m['AlertRuleContent'])
        if m.get('AlertStatus') is not None:
            self.alert_status = m.get('AlertStatus')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        self.annotations = []
        if m.get('Annotations') is not None:
            for k in m.get('Annotations'):
                temp_model = CreateOrUpdateAlertRuleResponseBodyAlertRuleAnnotations()
                self.annotations.append(temp_model.from_map(k))
        if m.get('AutoAddNewApplication') is not None:
            self.auto_add_new_application = m.get('AutoAddNewApplication')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Extend') is not None:
            self.extend = m.get('Extend')
        if m.get('Filters') is not None:
            temp_model = CreateOrUpdateAlertRuleResponseBodyAlertRuleFilters()
            self.filters = temp_model.from_map(m['Filters'])
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = CreateOrUpdateAlertRuleResponseBodyAlertRuleLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MetricsType') is not None:
            self.metrics_type = m.get('MetricsType')
        if m.get('NotifyStrategy') is not None:
            self.notify_strategy = m.get('NotifyStrategy')
        if m.get('Pids') is not None:
            self.pids = m.get('Pids')
        if m.get('PromQL') is not None:
            self.prom_ql = m.get('PromQL')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateOrUpdateAlertRuleResponseBody(TeaModel):
    def __init__(
        self,
        alert_rule: CreateOrUpdateAlertRuleResponseBodyAlertRule = None,
        request_id: str = None,
    ):
        self.alert_rule = alert_rule
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.alert_rule:
            self.alert_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_rule is not None:
            result['AlertRule'] = self.alert_rule.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertRule') is not None:
            temp_model = CreateOrUpdateAlertRuleResponseBodyAlertRule()
            self.alert_rule = temp_model.from_map(m['AlertRule'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateOrUpdateAlertRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateOrUpdateAlertRuleResponseBody = None,
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
            temp_model = CreateOrUpdateAlertRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrUpdateContactRequest(TeaModel):
    def __init__(
        self,
        contact_id: int = None,
        contact_name: str = None,
        email: str = None,
        phone: str = None,
    ):
        # 告警联系人ID
        self.contact_id = contact_id
        # 告警联系人名称
        self.contact_name = contact_name
        # 告警联系人邮箱
        self.email = email
        # 告警联系人手机号码
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.email is not None:
            result['Email'] = self.email
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class CreateOrUpdateContactResponseBodyAlertContact(TeaModel):
    def __init__(
        self,
        contact_id: float = None,
        contact_name: str = None,
        email: str = None,
        is_verify: bool = None,
        phone: str = None,
    ):
        # 告警联系人ID
        self.contact_id = contact_id
        # 告警联系人名称
        self.contact_name = contact_name
        # 告警联系人邮箱
        self.email = email
        # 手机号码验证标识
        self.is_verify = is_verify
        # 告警联系人手机号
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.email is not None:
            result['Email'] = self.email
        if self.is_verify is not None:
            result['IsVerify'] = self.is_verify
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('IsVerify') is not None:
            self.is_verify = m.get('IsVerify')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class CreateOrUpdateContactResponseBody(TeaModel):
    def __init__(
        self,
        alert_contact: CreateOrUpdateContactResponseBodyAlertContact = None,
        request_id: str = None,
    ):
        self.alert_contact = alert_contact
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.alert_contact:
            self.alert_contact.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_contact is not None:
            result['AlertContact'] = self.alert_contact.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertContact') is not None:
            temp_model = CreateOrUpdateContactResponseBodyAlertContact()
            self.alert_contact = temp_model.from_map(m['AlertContact'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateOrUpdateContactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateOrUpdateContactResponseBody = None,
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
            temp_model = CreateOrUpdateContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrUpdateContactGroupRequest(TeaModel):
    def __init__(
        self,
        contact_group_id: int = None,
        contact_group_name: str = None,
        contact_ids: str = None,
    ):
        # 告警联系人组ID
        self.contact_group_id = contact_group_id
        # 告警联系人组名称
        self.contact_group_name = contact_group_name
        # 告警联系人ids
        self.contact_ids = contact_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')
        return self


class CreateOrUpdateContactGroupResponseBodyAlertContactGroup(TeaModel):
    def __init__(
        self,
        contact_group_id: float = None,
        contact_group_name: str = None,
        contact_ids: str = None,
    ):
        # 告警联系人组ID
        self.contact_group_id = contact_group_id
        # 告警联系人组名称
        self.contact_group_name = contact_group_name
        # 告警联系人ids
        self.contact_ids = contact_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')
        return self


class CreateOrUpdateContactGroupResponseBody(TeaModel):
    def __init__(
        self,
        alert_contact_group: CreateOrUpdateContactGroupResponseBodyAlertContactGroup = None,
        request_id: str = None,
    ):
        self.alert_contact_group = alert_contact_group
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.alert_contact_group:
            self.alert_contact_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_contact_group is not None:
            result['AlertContactGroup'] = self.alert_contact_group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertContactGroup') is not None:
            temp_model = CreateOrUpdateContactGroupResponseBodyAlertContactGroup()
            self.alert_contact_group = temp_model.from_map(m['AlertContactGroup'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateOrUpdateContactGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateOrUpdateContactGroupResponseBody = None,
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
            temp_model = CreateOrUpdateContactGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrUpdateEventBridgeIntegrationRequest(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        access_secret: str = None,
        description: str = None,
        endpoint: str = None,
        event_bus_name: str = None,
        event_bus_region_id: str = None,
        id: int = None,
        name: str = None,
        source: str = None,
    ):
        self.access_key = access_key
        self.access_secret = access_secret
        self.description = description
        self.endpoint = endpoint
        self.event_bus_name = event_bus_name
        self.event_bus_region_id = event_bus_region_id
        self.id = id
        self.name = name
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.access_secret is not None:
            result['AccessSecret'] = self.access_secret
        if self.description is not None:
            result['Description'] = self.description
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_bus_region_id is not None:
            result['EventBusRegionId'] = self.event_bus_region_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('AccessSecret') is not None:
            self.access_secret = m.get('AccessSecret')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventBusRegionId') is not None:
            self.event_bus_region_id = m.get('EventBusRegionId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreateOrUpdateEventBridgeIntegrationResponseBodyEventBridgeIntegration(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        access_secret: str = None,
        description: str = None,
        endpoint: str = None,
        event_bus_name: str = None,
        event_bus_region_id: str = None,
        id: int = None,
        name: str = None,
        source: str = None,
    ):
        self.access_key = access_key
        self.access_secret = access_secret
        self.description = description
        self.endpoint = endpoint
        self.event_bus_name = event_bus_name
        self.event_bus_region_id = event_bus_region_id
        self.id = id
        self.name = name
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.access_secret is not None:
            result['AccessSecret'] = self.access_secret
        if self.description is not None:
            result['Description'] = self.description
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name
        if self.event_bus_region_id is not None:
            result['EventBusRegionId'] = self.event_bus_region_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('AccessSecret') is not None:
            self.access_secret = m.get('AccessSecret')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')
        if m.get('EventBusRegionId') is not None:
            self.event_bus_region_id = m.get('EventBusRegionId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreateOrUpdateEventBridgeIntegrationResponseBody(TeaModel):
    def __init__(
        self,
        event_bridge_integration: CreateOrUpdateEventBridgeIntegrationResponseBodyEventBridgeIntegration = None,
        request_id: str = None,
    ):
        self.event_bridge_integration = event_bridge_integration
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.event_bridge_integration:
            self.event_bridge_integration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bridge_integration is not None:
            result['EventBridgeIntegration'] = self.event_bridge_integration.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBridgeIntegration') is not None:
            temp_model = CreateOrUpdateEventBridgeIntegrationResponseBodyEventBridgeIntegration()
            self.event_bridge_integration = temp_model.from_map(m['EventBridgeIntegration'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateOrUpdateEventBridgeIntegrationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateOrUpdateEventBridgeIntegrationResponseBody = None,
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
            temp_model = CreateOrUpdateEventBridgeIntegrationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrUpdateIMRobotRequest(TeaModel):
    def __init__(
        self,
        daily_noc: bool = None,
        daily_noc_time: str = None,
        robot_address: str = None,
        robot_id: int = None,
        robot_name: str = None,
        type: str = None,
    ):
        # 是否发送每日统计信息
        self.daily_noc = daily_noc
        # 每日统计发送时间
        self.daily_noc_time = daily_noc_time
        # 告警机器人地址
        self.robot_address = robot_address
        # 告警机器人ID
        self.robot_id = robot_id
        # 告警机器人名称
        self.robot_name = robot_name
        # 告警机器人类型:dingding/wechat
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.daily_noc is not None:
            result['DailyNoc'] = self.daily_noc
        if self.daily_noc_time is not None:
            result['DailyNocTime'] = self.daily_noc_time
        if self.robot_address is not None:
            result['RobotAddress'] = self.robot_address
        if self.robot_id is not None:
            result['RobotId'] = self.robot_id
        if self.robot_name is not None:
            result['RobotName'] = self.robot_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DailyNoc') is not None:
            self.daily_noc = m.get('DailyNoc')
        if m.get('DailyNocTime') is not None:
            self.daily_noc_time = m.get('DailyNocTime')
        if m.get('RobotAddress') is not None:
            self.robot_address = m.get('RobotAddress')
        if m.get('RobotId') is not None:
            self.robot_id = m.get('RobotId')
        if m.get('RobotName') is not None:
            self.robot_name = m.get('RobotName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateOrUpdateIMRobotResponseBodyAlertRobot(TeaModel):
    def __init__(
        self,
        daily_noc: bool = None,
        daily_noc_time: str = None,
        robot_address: str = None,
        robot_id: float = None,
        robot_name: str = None,
        type: str = None,
    ):
        # 是否发送每日统计信息
        self.daily_noc = daily_noc
        # 每日统计发送时间
        self.daily_noc_time = daily_noc_time
        # 告警机器人地址
        self.robot_address = robot_address
        # 告警机器人ID
        self.robot_id = robot_id
        # 告警机器人名称
        self.robot_name = robot_name
        # 告警机器人类型:dingding/wechat
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.daily_noc is not None:
            result['DailyNoc'] = self.daily_noc
        if self.daily_noc_time is not None:
            result['DailyNocTime'] = self.daily_noc_time
        if self.robot_address is not None:
            result['RobotAddress'] = self.robot_address
        if self.robot_id is not None:
            result['RobotId'] = self.robot_id
        if self.robot_name is not None:
            result['RobotName'] = self.robot_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DailyNoc') is not None:
            self.daily_noc = m.get('DailyNoc')
        if m.get('DailyNocTime') is not None:
            self.daily_noc_time = m.get('DailyNocTime')
        if m.get('RobotAddress') is not None:
            self.robot_address = m.get('RobotAddress')
        if m.get('RobotId') is not None:
            self.robot_id = m.get('RobotId')
        if m.get('RobotName') is not None:
            self.robot_name = m.get('RobotName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateOrUpdateIMRobotResponseBody(TeaModel):
    def __init__(
        self,
        alert_robot: CreateOrUpdateIMRobotResponseBodyAlertRobot = None,
        request_id: str = None,
    ):
        self.alert_robot = alert_robot
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.alert_robot:
            self.alert_robot.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_robot is not None:
            result['AlertRobot'] = self.alert_robot.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertRobot') is not None:
            temp_model = CreateOrUpdateIMRobotResponseBodyAlertRobot()
            self.alert_robot = temp_model.from_map(m['AlertRobot'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateOrUpdateIMRobotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateOrUpdateIMRobotResponseBody = None,
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
            temp_model = CreateOrUpdateIMRobotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrUpdateNotificationPolicyRequest(TeaModel):
    def __init__(
        self,
        escalation_policy_id: int = None,
        group_rule: str = None,
        id: int = None,
        integration_id: int = None,
        matching_rules: str = None,
        name: str = None,
        notify_rule: str = None,
        notify_template: str = None,
        repeat: bool = None,
        repeat_interval: int = None,
        send_recover_message: bool = None,
    ):
        # 升级规则ID
        self.escalation_policy_id = escalation_policy_id
        # 分组规则
        self.group_rule = group_rule
        # 通知策略ID
        self.id = id
        # 集成ID
        self.integration_id = integration_id
        # 事件匹配规则列表
        self.matching_rules = matching_rules
        # 通知策略名称
        self.name = name
        # 通知规则,通知对象，必填
        self.notify_rule = notify_rule
        # 通知模板
        self.notify_template = notify_template
        # 是否重复通知,不填默认为true，需要必填重复通知时间间隔；false，需要必填升级规则ID
        self.repeat = repeat
        # 重复通知时间间隔,单位：s
        self.repeat_interval = repeat_interval
        # 是否发送恢,不填默认为：true复通知
        self.send_recover_message = send_recover_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.escalation_policy_id is not None:
            result['EscalationPolicyId'] = self.escalation_policy_id
        if self.group_rule is not None:
            result['GroupRule'] = self.group_rule
        if self.id is not None:
            result['Id'] = self.id
        if self.integration_id is not None:
            result['IntegrationId'] = self.integration_id
        if self.matching_rules is not None:
            result['MatchingRules'] = self.matching_rules
        if self.name is not None:
            result['Name'] = self.name
        if self.notify_rule is not None:
            result['NotifyRule'] = self.notify_rule
        if self.notify_template is not None:
            result['NotifyTemplate'] = self.notify_template
        if self.repeat is not None:
            result['Repeat'] = self.repeat
        if self.repeat_interval is not None:
            result['RepeatInterval'] = self.repeat_interval
        if self.send_recover_message is not None:
            result['SendRecoverMessage'] = self.send_recover_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EscalationPolicyId') is not None:
            self.escalation_policy_id = m.get('EscalationPolicyId')
        if m.get('GroupRule') is not None:
            self.group_rule = m.get('GroupRule')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IntegrationId') is not None:
            self.integration_id = m.get('IntegrationId')
        if m.get('MatchingRules') is not None:
            self.matching_rules = m.get('MatchingRules')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NotifyRule') is not None:
            self.notify_rule = m.get('NotifyRule')
        if m.get('NotifyTemplate') is not None:
            self.notify_template = m.get('NotifyTemplate')
        if m.get('Repeat') is not None:
            self.repeat = m.get('Repeat')
        if m.get('RepeatInterval') is not None:
            self.repeat_interval = m.get('RepeatInterval')
        if m.get('SendRecoverMessage') is not None:
            self.send_recover_message = m.get('SendRecoverMessage')
        return self


class CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyGroupRule(TeaModel):
    def __init__(
        self,
        group_interval: int = None,
        group_wait: int = None,
        grouping_fields: List[str] = None,
    ):
        # 分组间隔时间，选填，默认是30s
        self.group_interval = group_interval
        # 分组等待时间，选填，默认是5秒
        self.group_wait = group_wait
        # 分组字段,为空则不分组，默认按照alertname分组
        self.grouping_fields = grouping_fields

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_interval is not None:
            result['GroupInterval'] = self.group_interval
        if self.group_wait is not None:
            result['GroupWait'] = self.group_wait
        if self.grouping_fields is not None:
            result['GroupingFields'] = self.grouping_fields
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupInterval') is not None:
            self.group_interval = m.get('GroupInterval')
        if m.get('GroupWait') is not None:
            self.group_wait = m.get('GroupWait')
        if m.get('GroupingFields') is not None:
            self.grouping_fields = m.get('GroupingFields')
        return self


class CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyMatchingRulesMatchingConditions(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # 条件字段
        self.key = key
        # 对应关系
        self.operator = operator
        # 条件字段值
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
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyMatchingRules(TeaModel):
    def __init__(
        self,
        matching_conditions: List[CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyMatchingRulesMatchingConditions] = None,
    ):
        self.matching_conditions = matching_conditions

    def validate(self):
        if self.matching_conditions:
            for k in self.matching_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MatchingConditions'] = []
        if self.matching_conditions is not None:
            for k in self.matching_conditions:
                result['MatchingConditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.matching_conditions = []
        if m.get('MatchingConditions') is not None:
            for k in m.get('MatchingConditions'):
                temp_model = CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyMatchingRulesMatchingConditions()
                self.matching_conditions.append(temp_model.from_map(k))
        return self


class CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyRuleNotifyObjects(TeaModel):
    def __init__(
        self,
        notify_object_id: int = None,
        notify_object_name: str = None,
        notify_object_type: str = None,
    ):
        # 通知对象ID
        self.notify_object_id = notify_object_id
        # 通知对象名称
        self.notify_object_name = notify_object_name
        # 通知对象类型，CONTACT, CONTACT_GROUP, ARMS_CONTACT, DING_ROBOT
        self.notify_object_type = notify_object_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify_object_id is not None:
            result['NotifyObjectId'] = self.notify_object_id
        if self.notify_object_name is not None:
            result['NotifyObjectName'] = self.notify_object_name
        if self.notify_object_type is not None:
            result['NotifyObjectType'] = self.notify_object_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotifyObjectId') is not None:
            self.notify_object_id = m.get('NotifyObjectId')
        if m.get('NotifyObjectName') is not None:
            self.notify_object_name = m.get('NotifyObjectName')
        if m.get('NotifyObjectType') is not None:
            self.notify_object_type = m.get('NotifyObjectType')
        return self


class CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyRule(TeaModel):
    def __init__(
        self,
        notify_channels: List[str] = None,
        notify_end_time: str = None,
        notify_objects: List[CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyRuleNotifyObjects] = None,
        notify_start_time: str = None,
    ):
        # 通知渠道
        self.notify_channels = notify_channels
        # 通知时间段结束时间
        self.notify_end_time = notify_end_time
        # 通知对象
        self.notify_objects = notify_objects
        # 通知时间段开始时间
        self.notify_start_time = notify_start_time

    def validate(self):
        if self.notify_objects:
            for k in self.notify_objects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify_channels is not None:
            result['NotifyChannels'] = self.notify_channels
        if self.notify_end_time is not None:
            result['NotifyEndTime'] = self.notify_end_time
        result['NotifyObjects'] = []
        if self.notify_objects is not None:
            for k in self.notify_objects:
                result['NotifyObjects'].append(k.to_map() if k else None)
        if self.notify_start_time is not None:
            result['NotifyStartTime'] = self.notify_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotifyChannels') is not None:
            self.notify_channels = m.get('NotifyChannels')
        if m.get('NotifyEndTime') is not None:
            self.notify_end_time = m.get('NotifyEndTime')
        self.notify_objects = []
        if m.get('NotifyObjects') is not None:
            for k in m.get('NotifyObjects'):
                temp_model = CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyRuleNotifyObjects()
                self.notify_objects.append(temp_model.from_map(k))
        if m.get('NotifyStartTime') is not None:
            self.notify_start_time = m.get('NotifyStartTime')
        return self


class CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyTemplate(TeaModel):
    def __init__(
        self,
        email_content: str = None,
        email_recover_content: str = None,
        email_recover_title: str = None,
        email_title: str = None,
        robot_content: str = None,
        sms_content: str = None,
        sms_recover_content: str = None,
        tts_content: str = None,
        tts_recover_content: str = None,
    ):
        # 邮件内容
        self.email_content = email_content
        # 恢复告警邮件内容
        self.email_recover_content = email_recover_content
        # 恢复告警邮件标题
        self.email_recover_title = email_recover_title
        # 邮件标题
        self.email_title = email_title
        # 机器人告警内容
        self.robot_content = robot_content
        # 短信内容
        self.sms_content = sms_content
        # 恢复告警短信内容
        self.sms_recover_content = sms_recover_content
        # 智能语音告警内容
        self.tts_content = tts_content
        # 智能语音恢复告警内容
        self.tts_recover_content = tts_recover_content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email_content is not None:
            result['EmailContent'] = self.email_content
        if self.email_recover_content is not None:
            result['EmailRecoverContent'] = self.email_recover_content
        if self.email_recover_title is not None:
            result['EmailRecoverTitle'] = self.email_recover_title
        if self.email_title is not None:
            result['EmailTitle'] = self.email_title
        if self.robot_content is not None:
            result['RobotContent'] = self.robot_content
        if self.sms_content is not None:
            result['SmsContent'] = self.sms_content
        if self.sms_recover_content is not None:
            result['SmsRecoverContent'] = self.sms_recover_content
        if self.tts_content is not None:
            result['TtsContent'] = self.tts_content
        if self.tts_recover_content is not None:
            result['TtsRecoverContent'] = self.tts_recover_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmailContent') is not None:
            self.email_content = m.get('EmailContent')
        if m.get('EmailRecoverContent') is not None:
            self.email_recover_content = m.get('EmailRecoverContent')
        if m.get('EmailRecoverTitle') is not None:
            self.email_recover_title = m.get('EmailRecoverTitle')
        if m.get('EmailTitle') is not None:
            self.email_title = m.get('EmailTitle')
        if m.get('RobotContent') is not None:
            self.robot_content = m.get('RobotContent')
        if m.get('SmsContent') is not None:
            self.sms_content = m.get('SmsContent')
        if m.get('SmsRecoverContent') is not None:
            self.sms_recover_content = m.get('SmsRecoverContent')
        if m.get('TtsContent') is not None:
            self.tts_content = m.get('TtsContent')
        if m.get('TtsRecoverContent') is not None:
            self.tts_recover_content = m.get('TtsRecoverContent')
        return self


class CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicy(TeaModel):
    def __init__(
        self,
        escalation_policy_id: int = None,
        group_rule: CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyGroupRule = None,
        id: int = None,
        integration_id: int = None,
        matching_rules: List[CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyMatchingRules] = None,
        name: str = None,
        notify_rule: CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyRule = None,
        notify_template: CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyTemplate = None,
        repeat: bool = None,
        repeat_interval: int = None,
        send_recover_message: bool = None,
    ):
        # 升级规则ID
        self.escalation_policy_id = escalation_policy_id
        # 分组规则
        self.group_rule = group_rule
        # 通知策略ID
        self.id = id
        # 集成ID
        self.integration_id = integration_id
        # 事件匹配规则列表
        self.matching_rules = matching_rules
        # 通知策略名称
        self.name = name
        # 通知规则
        self.notify_rule = notify_rule
        # 通知模板
        self.notify_template = notify_template
        # 是否重复通知
        self.repeat = repeat
        # 重复通知时间间隔
        self.repeat_interval = repeat_interval
        # 是否发送恢复通知
        self.send_recover_message = send_recover_message

    def validate(self):
        if self.group_rule:
            self.group_rule.validate()
        if self.matching_rules:
            for k in self.matching_rules:
                if k:
                    k.validate()
        if self.notify_rule:
            self.notify_rule.validate()
        if self.notify_template:
            self.notify_template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.escalation_policy_id is not None:
            result['EscalationPolicyId'] = self.escalation_policy_id
        if self.group_rule is not None:
            result['GroupRule'] = self.group_rule.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.integration_id is not None:
            result['IntegrationId'] = self.integration_id
        result['MatchingRules'] = []
        if self.matching_rules is not None:
            for k in self.matching_rules:
                result['MatchingRules'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.notify_rule is not None:
            result['NotifyRule'] = self.notify_rule.to_map()
        if self.notify_template is not None:
            result['NotifyTemplate'] = self.notify_template.to_map()
        if self.repeat is not None:
            result['Repeat'] = self.repeat
        if self.repeat_interval is not None:
            result['RepeatInterval'] = self.repeat_interval
        if self.send_recover_message is not None:
            result['SendRecoverMessage'] = self.send_recover_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EscalationPolicyId') is not None:
            self.escalation_policy_id = m.get('EscalationPolicyId')
        if m.get('GroupRule') is not None:
            temp_model = CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyGroupRule()
            self.group_rule = temp_model.from_map(m['GroupRule'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IntegrationId') is not None:
            self.integration_id = m.get('IntegrationId')
        self.matching_rules = []
        if m.get('MatchingRules') is not None:
            for k in m.get('MatchingRules'):
                temp_model = CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyMatchingRules()
                self.matching_rules.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NotifyRule') is not None:
            temp_model = CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyRule()
            self.notify_rule = temp_model.from_map(m['NotifyRule'])
        if m.get('NotifyTemplate') is not None:
            temp_model = CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicyNotifyTemplate()
            self.notify_template = temp_model.from_map(m['NotifyTemplate'])
        if m.get('Repeat') is not None:
            self.repeat = m.get('Repeat')
        if m.get('RepeatInterval') is not None:
            self.repeat_interval = m.get('RepeatInterval')
        if m.get('SendRecoverMessage') is not None:
            self.send_recover_message = m.get('SendRecoverMessage')
        return self


class CreateOrUpdateNotificationPolicyResponseBody(TeaModel):
    def __init__(
        self,
        notification_policy: CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicy = None,
        request_id: str = None,
    ):
        # 通知策略对象
        self.notification_policy = notification_policy
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.notification_policy:
            self.notification_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notification_policy is not None:
            result['NotificationPolicy'] = self.notification_policy.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotificationPolicy') is not None:
            temp_model = CreateOrUpdateNotificationPolicyResponseBodyNotificationPolicy()
            self.notification_policy = temp_model.from_map(m['NotificationPolicy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateOrUpdateNotificationPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateOrUpdateNotificationPolicyResponseBody = None,
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
            temp_model = CreateOrUpdateNotificationPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrUpdateSilencePolicyRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        matching_rules: str = None,
        name: str = None,
    ):
        # 静默策略ID
        self.id = id
        # 分派规则
        self.matching_rules = matching_rules
        # 静默策略名称
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.matching_rules is not None:
            result['MatchingRules'] = self.matching_rules
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MatchingRules') is not None:
            self.matching_rules = m.get('MatchingRules')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateOrUpdateSilencePolicyResponseBodySilencePolicyMatchingRulesMatchingConditions(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # 条件字段
        self.key = key
        # 对应关系
        self.operator = operator
        # 条件字段值
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
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateOrUpdateSilencePolicyResponseBodySilencePolicyMatchingRules(TeaModel):
    def __init__(
        self,
        matching_conditions: List[CreateOrUpdateSilencePolicyResponseBodySilencePolicyMatchingRulesMatchingConditions] = None,
    ):
        # 分派条件
        self.matching_conditions = matching_conditions

    def validate(self):
        if self.matching_conditions:
            for k in self.matching_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MatchingConditions'] = []
        if self.matching_conditions is not None:
            for k in self.matching_conditions:
                result['MatchingConditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.matching_conditions = []
        if m.get('MatchingConditions') is not None:
            for k in m.get('MatchingConditions'):
                temp_model = CreateOrUpdateSilencePolicyResponseBodySilencePolicyMatchingRulesMatchingConditions()
                self.matching_conditions.append(temp_model.from_map(k))
        return self


class CreateOrUpdateSilencePolicyResponseBodySilencePolicy(TeaModel):
    def __init__(
        self,
        id: int = None,
        matching_rules: List[CreateOrUpdateSilencePolicyResponseBodySilencePolicyMatchingRules] = None,
        name: str = None,
    ):
        # 静默策略ID
        self.id = id
        # 分派规则
        self.matching_rules = matching_rules
        # 静默策略名称
        self.name = name

    def validate(self):
        if self.matching_rules:
            for k in self.matching_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        result['MatchingRules'] = []
        if self.matching_rules is not None:
            for k in self.matching_rules:
                result['MatchingRules'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.matching_rules = []
        if m.get('MatchingRules') is not None:
            for k in m.get('MatchingRules'):
                temp_model = CreateOrUpdateSilencePolicyResponseBodySilencePolicyMatchingRules()
                self.matching_rules.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateOrUpdateSilencePolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        silence_policy: CreateOrUpdateSilencePolicyResponseBodySilencePolicy = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 静默策略对象
        self.silence_policy = silence_policy

    def validate(self):
        if self.silence_policy:
            self.silence_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.silence_policy is not None:
            result['SilencePolicy'] = self.silence_policy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SilencePolicy') is not None:
            temp_model = CreateOrUpdateSilencePolicyResponseBodySilencePolicy()
            self.silence_policy = temp_model.from_map(m['SilencePolicy'])
        return self


class CreateOrUpdateSilencePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateOrUpdateSilencePolicyResponseBody = None,
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
            temp_model = CreateOrUpdateSilencePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrUpdateWebhookContactRequest(TeaModel):
    def __init__(
        self,
        biz_headers: str = None,
        biz_params: str = None,
        body: str = None,
        method: str = None,
        recover_body: str = None,
        url: str = None,
        webhook_id: int = None,
        webhook_name: str = None,
    ):
        # http请求头
        self.biz_headers = biz_headers
        # http请求参数
        self.biz_params = biz_params
        # 告警通知模板
        self.body = body
        # Http请求方法
        self.method = method
        # 告警恢复模板
        self.recover_body = recover_body
        # Url
        self.url = url
        # 告警webhook ID
        self.webhook_id = webhook_id
        # 告警webhook名称
        self.webhook_name = webhook_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_headers is not None:
            result['BizHeaders'] = self.biz_headers
        if self.biz_params is not None:
            result['BizParams'] = self.biz_params
        if self.body is not None:
            result['Body'] = self.body
        if self.method is not None:
            result['Method'] = self.method
        if self.recover_body is not None:
            result['RecoverBody'] = self.recover_body
        if self.url is not None:
            result['Url'] = self.url
        if self.webhook_id is not None:
            result['WebhookId'] = self.webhook_id
        if self.webhook_name is not None:
            result['WebhookName'] = self.webhook_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizHeaders') is not None:
            self.biz_headers = m.get('BizHeaders')
        if m.get('BizParams') is not None:
            self.biz_params = m.get('BizParams')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('RecoverBody') is not None:
            self.recover_body = m.get('RecoverBody')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('WebhookId') is not None:
            self.webhook_id = m.get('WebhookId')
        if m.get('WebhookName') is not None:
            self.webhook_name = m.get('WebhookName')
        return self


class CreateOrUpdateWebhookContactResponseBodyWebhookContactWebhook(TeaModel):
    def __init__(
        self,
        biz_headers: str = None,
        biz_params: str = None,
        body: str = None,
        method: str = None,
        recover_body: str = None,
        url: str = None,
    ):
        # http请求头
        self.biz_headers = biz_headers
        # http请求参数
        self.biz_params = biz_params
        # 告警通知模板
        self.body = body
        # Http请求方法
        self.method = method
        # 告警恢复模板
        self.recover_body = recover_body
        # url
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_headers is not None:
            result['BizHeaders'] = self.biz_headers
        if self.biz_params is not None:
            result['BizParams'] = self.biz_params
        if self.body is not None:
            result['Body'] = self.body
        if self.method is not None:
            result['Method'] = self.method
        if self.recover_body is not None:
            result['RecoverBody'] = self.recover_body
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizHeaders') is not None:
            self.biz_headers = m.get('BizHeaders')
        if m.get('BizParams') is not None:
            self.biz_params = m.get('BizParams')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('RecoverBody') is not None:
            self.recover_body = m.get('RecoverBody')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateOrUpdateWebhookContactResponseBodyWebhookContact(TeaModel):
    def __init__(
        self,
        webhook: CreateOrUpdateWebhookContactResponseBodyWebhookContactWebhook = None,
        webhook_id: float = None,
        webhook_name: str = None,
    ):
        self.webhook = webhook
        # 告警webhook ID
        self.webhook_id = webhook_id
        # 告警webhook名称
        self.webhook_name = webhook_name

    def validate(self):
        if self.webhook:
            self.webhook.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.webhook is not None:
            result['Webhook'] = self.webhook.to_map()
        if self.webhook_id is not None:
            result['WebhookId'] = self.webhook_id
        if self.webhook_name is not None:
            result['WebhookName'] = self.webhook_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Webhook') is not None:
            temp_model = CreateOrUpdateWebhookContactResponseBodyWebhookContactWebhook()
            self.webhook = temp_model.from_map(m['Webhook'])
        if m.get('WebhookId') is not None:
            self.webhook_id = m.get('WebhookId')
        if m.get('WebhookName') is not None:
            self.webhook_name = m.get('WebhookName')
        return self


class CreateOrUpdateWebhookContactResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        webhook_contact: CreateOrUpdateWebhookContactResponseBodyWebhookContact = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.webhook_contact = webhook_contact

    def validate(self):
        if self.webhook_contact:
            self.webhook_contact.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.webhook_contact is not None:
            result['WebhookContact'] = self.webhook_contact.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WebhookContact') is not None:
            temp_model = CreateOrUpdateWebhookContactResponseBodyWebhookContact()
            self.webhook_contact = temp_model.from_map(m['WebhookContact'])
        return self


class CreateOrUpdateWebhookContactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateOrUpdateWebhookContactResponseBody = None,
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
            temp_model = CreateOrUpdateWebhookContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePrometheusAlertRuleRequest(TeaModel):
    def __init__(
        self,
        alert_name: str = None,
        annotations: str = None,
        cluster_id: str = None,
        dispatch_rule_id: int = None,
        duration: str = None,
        expression: str = None,
        labels: str = None,
        message: str = None,
        notify_type: str = None,
        region_id: str = None,
        type: str = None,
    ):
        self.alert_name = alert_name
        self.annotations = annotations
        self.cluster_id = cluster_id
        self.dispatch_rule_id = dispatch_rule_id
        self.duration = duration
        self.expression = expression
        self.labels = labels
        self.message = message
        self.notify_type = notify_type
        self.region_id = region_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.annotations is not None:
            result['Annotations'] = self.annotations
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.message is not None:
            result['Message'] = self.message
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreatePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations(TeaModel):
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
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreatePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels(TeaModel):
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
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreatePrometheusAlertRuleResponseBodyPrometheusAlertRule(TeaModel):
    def __init__(
        self,
        alert_id: int = None,
        alert_name: str = None,
        annotations: List[CreatePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations] = None,
        cluster_id: str = None,
        dispatch_rule_id: int = None,
        duration: str = None,
        expression: str = None,
        labels: List[CreatePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels] = None,
        message: str = None,
        notify_type: str = None,
        status: int = None,
        type: str = None,
    ):
        self.alert_id = alert_id
        self.alert_name = alert_name
        self.annotations = annotations
        self.cluster_id = cluster_id
        self.dispatch_rule_id = dispatch_rule_id
        self.duration = duration
        self.expression = expression
        self.labels = labels
        self.message = message
        self.notify_type = notify_type
        self.status = status
        self.type = type

    def validate(self):
        if self.annotations:
            for k in self.annotations:
                if k:
                    k.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        result['Annotations'] = []
        if self.annotations is not None:
            for k in self.annotations:
                result['Annotations'].append(k.to_map() if k else None)
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expression is not None:
            result['Expression'] = self.expression
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        self.annotations = []
        if m.get('Annotations') is not None:
            for k in m.get('Annotations'):
                temp_model = CreatePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations()
                self.annotations.append(temp_model.from_map(k))
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = CreatePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreatePrometheusAlertRuleResponseBody(TeaModel):
    def __init__(
        self,
        prometheus_alert_rule: CreatePrometheusAlertRuleResponseBodyPrometheusAlertRule = None,
        request_id: str = None,
    ):
        self.prometheus_alert_rule = prometheus_alert_rule
        self.request_id = request_id

    def validate(self):
        if self.prometheus_alert_rule:
            self.prometheus_alert_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prometheus_alert_rule is not None:
            result['PrometheusAlertRule'] = self.prometheus_alert_rule.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrometheusAlertRule') is not None:
            temp_model = CreatePrometheusAlertRuleResponseBodyPrometheusAlertRule()
            self.prometheus_alert_rule = temp_model.from_map(m['PrometheusAlertRule'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePrometheusAlertRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePrometheusAlertRuleResponseBody = None,
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
            temp_model = CreatePrometheusAlertRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRetcodeAppRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        retcode_app_name: str = None,
        retcode_app_type: str = None,
    ):
        self.region_id = region_id
        self.retcode_app_name = retcode_app_name
        self.retcode_app_type = retcode_app_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.retcode_app_name is not None:
            result['RetcodeAppName'] = self.retcode_app_name
        if self.retcode_app_type is not None:
            result['RetcodeAppType'] = self.retcode_app_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RetcodeAppName') is not None:
            self.retcode_app_name = m.get('RetcodeAppName')
        if m.get('RetcodeAppType') is not None:
            self.retcode_app_type = m.get('RetcodeAppType')
        return self


class CreateRetcodeAppResponseBodyRetcodeAppDataBean(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        pid: str = None,
    ):
        self.app_id = app_id
        self.pid = pid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.pid is not None:
            result['Pid'] = self.pid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        return self


class CreateRetcodeAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        retcode_app_data_bean: CreateRetcodeAppResponseBodyRetcodeAppDataBean = None,
    ):
        self.request_id = request_id
        self.retcode_app_data_bean = retcode_app_data_bean

    def validate(self):
        if self.retcode_app_data_bean:
            self.retcode_app_data_bean.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.retcode_app_data_bean is not None:
            result['RetcodeAppDataBean'] = self.retcode_app_data_bean.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RetcodeAppDataBean') is not None:
            temp_model = CreateRetcodeAppResponseBodyRetcodeAppDataBean()
            self.retcode_app_data_bean = temp_model.from_map(m['RetcodeAppDataBean'])
        return self


class CreateRetcodeAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRetcodeAppResponseBody = None,
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
            temp_model = CreateRetcodeAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWebhookRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        contact_name: str = None,
        http_headers: str = None,
        http_params: str = None,
        method: str = None,
        recover_body: str = None,
        region_id: str = None,
        url: str = None,
    ):
        self.body = body
        self.contact_name = contact_name
        self.http_headers = http_headers
        self.http_params = http_params
        self.method = method
        self.recover_body = recover_body
        self.region_id = region_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.http_headers is not None:
            result['HttpHeaders'] = self.http_headers
        if self.http_params is not None:
            result['HttpParams'] = self.http_params
        if self.method is not None:
            result['Method'] = self.method
        if self.recover_body is not None:
            result['RecoverBody'] = self.recover_body
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('HttpHeaders') is not None:
            self.http_headers = m.get('HttpHeaders')
        if m.get('HttpParams') is not None:
            self.http_params = m.get('HttpParams')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('RecoverBody') is not None:
            self.recover_body = m.get('RecoverBody')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateWebhookResponseBody(TeaModel):
    def __init__(
        self,
        contact_id: str = None,
        request_id: str = None,
    ):
        self.contact_id = contact_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateWebhookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateWebhookResponseBody = None,
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
            temp_model = CreateWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteASMIntegrationRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteASMIntegrationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        state: bool = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DeleteASMIntegrationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteASMIntegrationResponseBody = None,
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
            temp_model = DeleteASMIntegrationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlertContactRequest(TeaModel):
    def __init__(
        self,
        contact_id: int = None,
        region_id: str = None,
    ):
        self.contact_id = contact_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAlertContactResponseBody(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAlertContactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAlertContactResponseBody = None,
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
            temp_model = DeleteAlertContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlertContactGroupRequest(TeaModel):
    def __init__(
        self,
        contact_group_id: int = None,
        region_id: str = None,
    ):
        self.contact_group_id = contact_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAlertContactGroupResponseBody(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAlertContactGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAlertContactGroupResponseBody = None,
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
            temp_model = DeleteAlertContactGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlertRuleRequest(TeaModel):
    def __init__(
        self,
        alert_id: int = None,
    ):
        # 告警规则ID
        self.alert_id = alert_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        return self


class DeleteAlertRuleResponseBody(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.is_success = is_success
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAlertRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAlertRuleResponseBody = None,
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
            temp_model = DeleteAlertRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlertRulesRequest(TeaModel):
    def __init__(
        self,
        alert_ids: str = None,
        region_id: str = None,
    ):
        self.alert_ids = alert_ids
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_ids is not None:
            result['AlertIds'] = self.alert_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertIds') is not None:
            self.alert_ids = m.get('AlertIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAlertRulesResponseBody(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAlertRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAlertRulesResponseBody = None,
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
            temp_model = DeleteAlertRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCmsExporterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteCmsExporterResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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


class DeleteCmsExporterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCmsExporterResponseBody = None,
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
            temp_model = DeleteCmsExporterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteContactRequest(TeaModel):
    def __init__(
        self,
        contact_id: int = None,
    ):
        # 告警联系人ID
        self.contact_id = contact_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        return self


class DeleteContactResponseBody(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.is_success = is_success
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteContactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteContactResponseBody = None,
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
            temp_model = DeleteContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteContactGroupRequest(TeaModel):
    def __init__(
        self,
        contact_group_id: int = None,
    ):
        # 告警联系人组ID
        self.contact_group_id = contact_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')
        return self


class DeleteContactGroupResponseBody(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.is_success = is_success
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteContactGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteContactGroupResponseBody = None,
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
            temp_model = DeleteContactGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDispatchRuleRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        region_id: str = None,
    ):
        self.id = id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDispatchRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDispatchRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDispatchRuleResponseBody = None,
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
            temp_model = DeleteDispatchRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEventBridgeIntegrationRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteEventBridgeIntegrationResponseBody(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.is_success = is_success
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteEventBridgeIntegrationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteEventBridgeIntegrationResponseBody = None,
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
            temp_model = DeleteEventBridgeIntegrationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIMRobotRequest(TeaModel):
    def __init__(
        self,
        robot_id: int = None,
    ):
        # 告警机器人ID
        self.robot_id = robot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.robot_id is not None:
            result['RobotId'] = self.robot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RobotId') is not None:
            self.robot_id = m.get('RobotId')
        return self


class DeleteIMRobotResponseBody(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.is_success = is_success
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteIMRobotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteIMRobotResponseBody = None,
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
            temp_model = DeleteIMRobotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIntegrationRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        integration: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.integration = integration
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.integration is not None:
            result['Integration'] = self.integration
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Integration') is not None:
            self.integration = m.get('Integration')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteIntegrationResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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


class DeleteIntegrationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteIntegrationResponseBody = None,
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
            temp_model = DeleteIntegrationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNotificationPolicyRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        # 通知策略ID
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteNotificationPolicyResponseBody(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.is_success = is_success
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteNotificationPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteNotificationPolicyResponseBody = None,
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
            temp_model = DeleteNotificationPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePrometheusAlertRuleRequest(TeaModel):
    def __init__(
        self,
        alert_id: int = None,
    ):
        self.alert_id = alert_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        return self


class DeletePrometheusAlertRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeletePrometheusAlertRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePrometheusAlertRuleResponseBody = None,
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
            temp_model = DeletePrometheusAlertRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePrometheusGlobalViewRequest(TeaModel):
    def __init__(
        self,
        global_view_cluster_id: str = None,
        region_id: str = None,
    ):
        self.global_view_cluster_id = global_view_cluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.global_view_cluster_id is not None:
            result['GlobalViewClusterId'] = self.global_view_cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GlobalViewClusterId') is not None:
            self.global_view_cluster_id = m.get('GlobalViewClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeletePrometheusGlobalViewResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
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


class DeletePrometheusGlobalViewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePrometheusGlobalViewResponseBody = None,
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
            temp_model = DeletePrometheusGlobalViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRetcodeAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        region_id: str = None,
    ):
        self.app_id = app_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteRetcodeAppResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
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


class DeleteRetcodeAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRetcodeAppResponseBody = None,
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
            temp_model = DeleteRetcodeAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScenarioRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        scenario_id: int = None,
    ):
        self.region_id = region_id
        self.scenario_id = scenario_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        return self


class DeleteScenarioResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteScenarioResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteScenarioResponseBody = None,
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
            temp_model = DeleteScenarioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSilencePolicyRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        # 静默策略ID
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteSilencePolicyResponseBody(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        request_id: str = None,
    ):
        # 删除静默策略是否成功
        self.is_success = is_success
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSilencePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSilencePolicyResponseBody = None,
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
            temp_model = DeleteSilencePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTraceAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        pid: str = None,
        region_id: str = None,
        type: str = None,
    ):
        self.app_id = app_id
        self.pid = pid
        self.region_id = region_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DeleteTraceAppResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
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


class DeleteTraceAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTraceAppResponseBody = None,
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
            temp_model = DeleteTraceAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWebhookContactRequest(TeaModel):
    def __init__(
        self,
        webhook_id: int = None,
    ):
        # 告警webhookID
        self.webhook_id = webhook_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.webhook_id is not None:
            result['WebhookId'] = self.webhook_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WebhookId') is not None:
            self.webhook_id = m.get('WebhookId')
        return self


class DeleteWebhookContactResponseBody(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.is_success = is_success
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteWebhookContactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteWebhookContactResponseBody = None,
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
            temp_model = DeleteWebhookContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContactGroupsRequest(TeaModel):
    def __init__(
        self,
        contact_group_name: str = None,
        is_detail: bool = None,
        page: int = None,
        size: int = None,
    ):
        # 告警联系人组名称
        self.contact_group_name = contact_group_name
        # 是否返回联系人分组中包含的所有联系人。默认不返回所有联系人。
        self.is_detail = is_detail
        self.page = page
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        if self.is_detail is not None:
            result['IsDetail'] = self.is_detail
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        if m.get('IsDetail') is not None:
            self.is_detail = m.get('IsDetail')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeContactGroupsResponseBodyPageBeanAlertContactGroupsContacts(TeaModel):
    def __init__(
        self,
        contact_id: float = None,
        contact_name: str = None,
        email: str = None,
        phone: str = None,
    ):
        # 联系人ID
        self.contact_id = contact_id
        # 联系人名称
        self.contact_name = contact_name
        # 联系人邮箱
        self.email = email
        # 联系人手机号码
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.email is not None:
            result['Email'] = self.email
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class DescribeContactGroupsResponseBodyPageBeanAlertContactGroups(TeaModel):
    def __init__(
        self,
        contact_group_id: float = None,
        contact_group_name: str = None,
        contacts: List[DescribeContactGroupsResponseBodyPageBeanAlertContactGroupsContacts] = None,
    ):
        # 告警联系人组ID
        self.contact_group_id = contact_group_id
        # 告警联系人组名称
        self.contact_group_name = contact_group_name
        # 联系人对象
        self.contacts = contacts

    def validate(self):
        if self.contacts:
            for k in self.contacts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        result['Contacts'] = []
        if self.contacts is not None:
            for k in self.contacts:
                result['Contacts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        self.contacts = []
        if m.get('Contacts') is not None:
            for k in m.get('Contacts'):
                temp_model = DescribeContactGroupsResponseBodyPageBeanAlertContactGroupsContacts()
                self.contacts.append(temp_model.from_map(k))
        return self


class DescribeContactGroupsResponseBodyPageBean(TeaModel):
    def __init__(
        self,
        alert_contact_groups: List[DescribeContactGroupsResponseBodyPageBeanAlertContactGroups] = None,
        page: int = None,
        size: int = None,
        total: int = None,
    ):
        # 告警联系人组列表
        self.alert_contact_groups = alert_contact_groups
        # 页数
        self.page = page
        # 每一页数目
        self.size = size
        # 总数
        self.total = total

    def validate(self):
        if self.alert_contact_groups:
            for k in self.alert_contact_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlertContactGroups'] = []
        if self.alert_contact_groups is not None:
            for k in self.alert_contact_groups:
                result['AlertContactGroups'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_contact_groups = []
        if m.get('AlertContactGroups') is not None:
            for k in m.get('AlertContactGroups'):
                temp_model = DescribeContactGroupsResponseBodyPageBeanAlertContactGroups()
                self.alert_contact_groups.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeContactGroupsResponseBody(TeaModel):
    def __init__(
        self,
        page_bean: DescribeContactGroupsResponseBodyPageBean = None,
        request_id: str = None,
    ):
        # 分页对象
        self.page_bean = page_bean
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = DescribeContactGroupsResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeContactGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeContactGroupsResponseBody = None,
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
            temp_model = DescribeContactGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContactsRequest(TeaModel):
    def __init__(
        self,
        contact_name: str = None,
        email: str = None,
        page: int = None,
        phone: str = None,
        size: int = None,
    ):
        # 告警联系人名称
        self.contact_name = contact_name
        # 告警联系人邮箱
        self.email = email
        self.page = page
        # 告警联系人手机号码
        self.phone = phone
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.email is not None:
            result['Email'] = self.email
        if self.page is not None:
            result['Page'] = self.page
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeContactsResponseBodyPageBeanAlertContacts(TeaModel):
    def __init__(
        self,
        contact_id: float = None,
        contact_name: str = None,
        email: str = None,
        is_verify: bool = None,
        phone: str = None,
    ):
        # 告警联系人ID
        self.contact_id = contact_id
        # 告警联系人名称
        self.contact_name = contact_name
        # 告警联系人邮箱
        self.email = email
        # 手机号码是否验证标识
        self.is_verify = is_verify
        # 告警联系人手机号码
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.email is not None:
            result['Email'] = self.email
        if self.is_verify is not None:
            result['IsVerify'] = self.is_verify
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('IsVerify') is not None:
            self.is_verify = m.get('IsVerify')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class DescribeContactsResponseBodyPageBean(TeaModel):
    def __init__(
        self,
        alert_contacts: List[DescribeContactsResponseBodyPageBeanAlertContacts] = None,
        page: int = None,
        size: int = None,
        total: int = None,
    ):
        # 告警联系人列表
        self.alert_contacts = alert_contacts
        # 页数
        self.page = page
        # 每一页大小
        self.size = size
        # 总数
        self.total = total

    def validate(self):
        if self.alert_contacts:
            for k in self.alert_contacts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlertContacts'] = []
        if self.alert_contacts is not None:
            for k in self.alert_contacts:
                result['AlertContacts'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_contacts = []
        if m.get('AlertContacts') is not None:
            for k in m.get('AlertContacts'):
                temp_model = DescribeContactsResponseBodyPageBeanAlertContacts()
                self.alert_contacts.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeContactsResponseBody(TeaModel):
    def __init__(
        self,
        page_bean: DescribeContactsResponseBodyPageBean = None,
        request_id: str = None,
    ):
        # 分页对象
        self.page_bean = page_bean
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = DescribeContactsResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeContactsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeContactsResponseBody = None,
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
            temp_model = DescribeContactsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDispatchRuleRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        region_id: str = None,
    ):
        self.id = id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDispatchRuleResponseBodyDispatchRuleGroupRules(TeaModel):
    def __init__(
        self,
        group_id: int = None,
        group_interval: int = None,
        group_wait_time: int = None,
        grouping_fields: List[str] = None,
        repeat_interval: int = None,
    ):
        self.group_id = group_id
        self.group_interval = group_interval
        self.group_wait_time = group_wait_time
        self.grouping_fields = grouping_fields
        self.repeat_interval = repeat_interval

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_interval is not None:
            result['GroupInterval'] = self.group_interval
        if self.group_wait_time is not None:
            result['GroupWaitTime'] = self.group_wait_time
        if self.grouping_fields is not None:
            result['GroupingFields'] = self.grouping_fields
        if self.repeat_interval is not None:
            result['RepeatInterval'] = self.repeat_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupInterval') is not None:
            self.group_interval = m.get('GroupInterval')
        if m.get('GroupWaitTime') is not None:
            self.group_wait_time = m.get('GroupWaitTime')
        if m.get('GroupingFields') is not None:
            self.grouping_fields = m.get('GroupingFields')
        if m.get('RepeatInterval') is not None:
            self.repeat_interval = m.get('RepeatInterval')
        return self


class DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupsLabelMatchExpressions(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        self.key = key
        self.operator = operator
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
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroups(TeaModel):
    def __init__(
        self,
        label_match_expressions: List[DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupsLabelMatchExpressions] = None,
    ):
        self.label_match_expressions = label_match_expressions

    def validate(self):
        if self.label_match_expressions:
            for k in self.label_match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LabelMatchExpressions'] = []
        if self.label_match_expressions is not None:
            for k in self.label_match_expressions:
                result['LabelMatchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.label_match_expressions = []
        if m.get('LabelMatchExpressions') is not None:
            for k in m.get('LabelMatchExpressions'):
                temp_model = DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupsLabelMatchExpressions()
                self.label_match_expressions.append(temp_model.from_map(k))
        return self


class DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGrid(TeaModel):
    def __init__(
        self,
        label_match_expression_groups: List[DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroups] = None,
    ):
        self.label_match_expression_groups = label_match_expression_groups

    def validate(self):
        if self.label_match_expression_groups:
            for k in self.label_match_expression_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LabelMatchExpressionGroups'] = []
        if self.label_match_expression_groups is not None:
            for k in self.label_match_expression_groups:
                result['LabelMatchExpressionGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.label_match_expression_groups = []
        if m.get('LabelMatchExpressionGroups') is not None:
            for k in m.get('LabelMatchExpressionGroups'):
                temp_model = DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroups()
                self.label_match_expression_groups.append(temp_model.from_map(k))
        return self


class DescribeDispatchRuleResponseBodyDispatchRuleNotifyRulesNotifyObjects(TeaModel):
    def __init__(
        self,
        name: str = None,
        notify_object_id: str = None,
        notify_type: str = None,
    ):
        self.name = name
        self.notify_object_id = notify_object_id
        self.notify_type = notify_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.notify_object_id is not None:
            result['NotifyObjectId'] = self.notify_object_id
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NotifyObjectId') is not None:
            self.notify_object_id = m.get('NotifyObjectId')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        return self


class DescribeDispatchRuleResponseBodyDispatchRuleNotifyRules(TeaModel):
    def __init__(
        self,
        notify_channels: List[str] = None,
        notify_objects: List[DescribeDispatchRuleResponseBodyDispatchRuleNotifyRulesNotifyObjects] = None,
    ):
        self.notify_channels = notify_channels
        self.notify_objects = notify_objects

    def validate(self):
        if self.notify_objects:
            for k in self.notify_objects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify_channels is not None:
            result['NotifyChannels'] = self.notify_channels
        result['NotifyObjects'] = []
        if self.notify_objects is not None:
            for k in self.notify_objects:
                result['NotifyObjects'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotifyChannels') is not None:
            self.notify_channels = m.get('NotifyChannels')
        self.notify_objects = []
        if m.get('NotifyObjects') is not None:
            for k in m.get('NotifyObjects'):
                temp_model = DescribeDispatchRuleResponseBodyDispatchRuleNotifyRulesNotifyObjects()
                self.notify_objects.append(temp_model.from_map(k))
        return self


class DescribeDispatchRuleResponseBodyDispatchRule(TeaModel):
    def __init__(
        self,
        dispatch_type: str = None,
        group_rules: List[DescribeDispatchRuleResponseBodyDispatchRuleGroupRules] = None,
        is_recover: bool = None,
        label_match_expression_grid: DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGrid = None,
        name: str = None,
        notify_rules: List[DescribeDispatchRuleResponseBodyDispatchRuleNotifyRules] = None,
        rule_id: int = None,
        state: str = None,
    ):
        self.dispatch_type = dispatch_type
        self.group_rules = group_rules
        self.is_recover = is_recover
        self.label_match_expression_grid = label_match_expression_grid
        self.name = name
        self.notify_rules = notify_rules
        self.rule_id = rule_id
        self.state = state

    def validate(self):
        if self.group_rules:
            for k in self.group_rules:
                if k:
                    k.validate()
        if self.label_match_expression_grid:
            self.label_match_expression_grid.validate()
        if self.notify_rules:
            for k in self.notify_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dispatch_type is not None:
            result['DispatchType'] = self.dispatch_type
        result['GroupRules'] = []
        if self.group_rules is not None:
            for k in self.group_rules:
                result['GroupRules'].append(k.to_map() if k else None)
        if self.is_recover is not None:
            result['IsRecover'] = self.is_recover
        if self.label_match_expression_grid is not None:
            result['LabelMatchExpressionGrid'] = self.label_match_expression_grid.to_map()
        if self.name is not None:
            result['Name'] = self.name
        result['NotifyRules'] = []
        if self.notify_rules is not None:
            for k in self.notify_rules:
                result['NotifyRules'].append(k.to_map() if k else None)
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DispatchType') is not None:
            self.dispatch_type = m.get('DispatchType')
        self.group_rules = []
        if m.get('GroupRules') is not None:
            for k in m.get('GroupRules'):
                temp_model = DescribeDispatchRuleResponseBodyDispatchRuleGroupRules()
                self.group_rules.append(temp_model.from_map(k))
        if m.get('IsRecover') is not None:
            self.is_recover = m.get('IsRecover')
        if m.get('LabelMatchExpressionGrid') is not None:
            temp_model = DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGrid()
            self.label_match_expression_grid = temp_model.from_map(m['LabelMatchExpressionGrid'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.notify_rules = []
        if m.get('NotifyRules') is not None:
            for k in m.get('NotifyRules'):
                temp_model = DescribeDispatchRuleResponseBodyDispatchRuleNotifyRules()
                self.notify_rules.append(temp_model.from_map(k))
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeDispatchRuleResponseBody(TeaModel):
    def __init__(
        self,
        dispatch_rule: DescribeDispatchRuleResponseBodyDispatchRule = None,
        request_id: str = None,
    ):
        self.dispatch_rule = dispatch_rule
        self.request_id = request_id

    def validate(self):
        if self.dispatch_rule:
            self.dispatch_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dispatch_rule is not None:
            result['DispatchRule'] = self.dispatch_rule.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DispatchRule') is not None:
            temp_model = DescribeDispatchRuleResponseBodyDispatchRule()
            self.dispatch_rule = temp_model.from_map(m['DispatchRule'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDispatchRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDispatchRuleResponseBody = None,
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
            temp_model = DescribeDispatchRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIMRobotsRequest(TeaModel):
    def __init__(
        self,
        page: int = None,
        robot_name: str = None,
        size: int = None,
    ):
        self.page = page
        # 告警机器人名称
        self.robot_name = robot_name
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.robot_name is not None:
            result['RobotName'] = self.robot_name
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('RobotName') is not None:
            self.robot_name = m.get('RobotName')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeIMRobotsResponseBodyPageBeanAlertIMRobots(TeaModel):
    def __init__(
        self,
        daily_noc: bool = None,
        daily_noc_time: str = None,
        robot_addr: str = None,
        robot_id: float = None,
        robot_name: str = None,
        type: str = None,
    ):
        # 是否发送每日统计信息
        self.daily_noc = daily_noc
        # 每日统计发送时间
        self.daily_noc_time = daily_noc_time
        # 告警机器人地址
        self.robot_addr = robot_addr
        # 告警机器人ID
        self.robot_id = robot_id
        # 告警机器人名称
        self.robot_name = robot_name
        # 告警机器人类型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.daily_noc is not None:
            result['DailyNoc'] = self.daily_noc
        if self.daily_noc_time is not None:
            result['DailyNocTime'] = self.daily_noc_time
        if self.robot_addr is not None:
            result['RobotAddr'] = self.robot_addr
        if self.robot_id is not None:
            result['RobotId'] = self.robot_id
        if self.robot_name is not None:
            result['RobotName'] = self.robot_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DailyNoc') is not None:
            self.daily_noc = m.get('DailyNoc')
        if m.get('DailyNocTime') is not None:
            self.daily_noc_time = m.get('DailyNocTime')
        if m.get('RobotAddr') is not None:
            self.robot_addr = m.get('RobotAddr')
        if m.get('RobotId') is not None:
            self.robot_id = m.get('RobotId')
        if m.get('RobotName') is not None:
            self.robot_name = m.get('RobotName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeIMRobotsResponseBodyPageBean(TeaModel):
    def __init__(
        self,
        alert_imrobots: List[DescribeIMRobotsResponseBodyPageBeanAlertIMRobots] = None,
        page: int = None,
        size: int = None,
        total: int = None,
    ):
        self.alert_imrobots = alert_imrobots
        # 页数
        self.page = page
        # 每一页数目
        self.size = size
        # 总数
        self.total = total

    def validate(self):
        if self.alert_imrobots:
            for k in self.alert_imrobots:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlertIMRobots'] = []
        if self.alert_imrobots is not None:
            for k in self.alert_imrobots:
                result['AlertIMRobots'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_imrobots = []
        if m.get('AlertIMRobots') is not None:
            for k in m.get('AlertIMRobots'):
                temp_model = DescribeIMRobotsResponseBodyPageBeanAlertIMRobots()
                self.alert_imrobots.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeIMRobotsResponseBody(TeaModel):
    def __init__(
        self,
        page_bean: DescribeIMRobotsResponseBodyPageBean = None,
        request_id: str = None,
    ):
        # 分页对象
        self.page_bean = page_bean
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = DescribeIMRobotsResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeIMRobotsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeIMRobotsResponseBody = None,
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
            temp_model = DescribeIMRobotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePrometheusAlertRuleRequest(TeaModel):
    def __init__(
        self,
        alert_id: int = None,
    ):
        self.alert_id = alert_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        return self


class DescribePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations(TeaModel):
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
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels(TeaModel):
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
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribePrometheusAlertRuleResponseBodyPrometheusAlertRule(TeaModel):
    def __init__(
        self,
        alert_id: int = None,
        alert_name: str = None,
        annotations: List[DescribePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations] = None,
        cluster_id: str = None,
        dispatch_rule_id: int = None,
        duration: str = None,
        expression: str = None,
        labels: List[DescribePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels] = None,
        message: str = None,
        notify_type: str = None,
        status: int = None,
        type: str = None,
    ):
        self.alert_id = alert_id
        self.alert_name = alert_name
        self.annotations = annotations
        self.cluster_id = cluster_id
        self.dispatch_rule_id = dispatch_rule_id
        self.duration = duration
        self.expression = expression
        self.labels = labels
        self.message = message
        self.notify_type = notify_type
        self.status = status
        self.type = type

    def validate(self):
        if self.annotations:
            for k in self.annotations:
                if k:
                    k.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        result['Annotations'] = []
        if self.annotations is not None:
            for k in self.annotations:
                result['Annotations'].append(k.to_map() if k else None)
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expression is not None:
            result['Expression'] = self.expression
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        self.annotations = []
        if m.get('Annotations') is not None:
            for k in m.get('Annotations'):
                temp_model = DescribePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations()
                self.annotations.append(temp_model.from_map(k))
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = DescribePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribePrometheusAlertRuleResponseBody(TeaModel):
    def __init__(
        self,
        prometheus_alert_rule: DescribePrometheusAlertRuleResponseBodyPrometheusAlertRule = None,
        request_id: str = None,
    ):
        self.prometheus_alert_rule = prometheus_alert_rule
        self.request_id = request_id

    def validate(self):
        if self.prometheus_alert_rule:
            self.prometheus_alert_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prometheus_alert_rule is not None:
            result['PrometheusAlertRule'] = self.prometheus_alert_rule.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrometheusAlertRule') is not None:
            temp_model = DescribePrometheusAlertRuleResponseBodyPrometheusAlertRule()
            self.prometheus_alert_rule = temp_model.from_map(m['PrometheusAlertRule'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePrometheusAlertRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePrometheusAlertRuleResponseBody = None,
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
            temp_model = DescribePrometheusAlertRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTraceLicenseKeyRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeTraceLicenseKeyResponseBody(TeaModel):
    def __init__(
        self,
        license_key: str = None,
        request_id: str = None,
    ):
        self.license_key = license_key
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.license_key is not None:
            result['LicenseKey'] = self.license_key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LicenseKey') is not None:
            self.license_key = m.get('LicenseKey')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeTraceLicenseKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTraceLicenseKeyResponseBody = None,
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
            temp_model = DescribeTraceLicenseKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebhookContactsRequest(TeaModel):
    def __init__(
        self,
        page: int = None,
        size: int = None,
        webhook_name: str = None,
    ):
        self.page = page
        self.size = size
        # 告警webhook名称
        self.webhook_name = webhook_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.webhook_name is not None:
            result['WebhookName'] = self.webhook_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('WebhookName') is not None:
            self.webhook_name = m.get('WebhookName')
        return self


class DescribeWebhookContactsResponseBodyPageBeanWebhookContactsWebhook(TeaModel):
    def __init__(
        self,
        biz_headers: Dict[str, Any] = None,
        biz_params: Dict[str, Any] = None,
        body: str = None,
        method: str = None,
        recover_body: str = None,
        url: str = None,
    ):
        # HTTP请求头
        self.biz_headers = biz_headers
        # HTTP请求参数
        self.biz_params = biz_params
        # 告警通知模板
        self.body = body
        # http请求方式
        self.method = method
        # 告警恢复模板
        self.recover_body = recover_body
        # Url
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_headers is not None:
            result['BizHeaders'] = self.biz_headers
        if self.biz_params is not None:
            result['BizParams'] = self.biz_params
        if self.body is not None:
            result['Body'] = self.body
        if self.method is not None:
            result['Method'] = self.method
        if self.recover_body is not None:
            result['RecoverBody'] = self.recover_body
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizHeaders') is not None:
            self.biz_headers = m.get('BizHeaders')
        if m.get('BizParams') is not None:
            self.biz_params = m.get('BizParams')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('RecoverBody') is not None:
            self.recover_body = m.get('RecoverBody')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeWebhookContactsResponseBodyPageBeanWebhookContacts(TeaModel):
    def __init__(
        self,
        webhook: DescribeWebhookContactsResponseBodyPageBeanWebhookContactsWebhook = None,
        webhook_id: float = None,
        webhook_name: str = None,
    ):
        # webhook对象
        self.webhook = webhook
        # 告警webhookID
        self.webhook_id = webhook_id
        # 告警webhook名称
        self.webhook_name = webhook_name

    def validate(self):
        if self.webhook:
            self.webhook.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.webhook is not None:
            result['Webhook'] = self.webhook.to_map()
        if self.webhook_id is not None:
            result['WebhookId'] = self.webhook_id
        if self.webhook_name is not None:
            result['WebhookName'] = self.webhook_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Webhook') is not None:
            temp_model = DescribeWebhookContactsResponseBodyPageBeanWebhookContactsWebhook()
            self.webhook = temp_model.from_map(m['Webhook'])
        if m.get('WebhookId') is not None:
            self.webhook_id = m.get('WebhookId')
        if m.get('WebhookName') is not None:
            self.webhook_name = m.get('WebhookName')
        return self


class DescribeWebhookContactsResponseBodyPageBean(TeaModel):
    def __init__(
        self,
        page: int = None,
        size: int = None,
        total: int = None,
        webhook_contacts: List[DescribeWebhookContactsResponseBodyPageBeanWebhookContacts] = None,
    ):
        # 页数
        self.page = page
        # 每一页数目
        self.size = size
        # 总数
        self.total = total
        # 告警webhook联系人列表
        self.webhook_contacts = webhook_contacts

    def validate(self):
        if self.webhook_contacts:
            for k in self.webhook_contacts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        result['WebhookContacts'] = []
        if self.webhook_contacts is not None:
            for k in self.webhook_contacts:
                result['WebhookContacts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.webhook_contacts = []
        if m.get('WebhookContacts') is not None:
            for k in m.get('WebhookContacts'):
                temp_model = DescribeWebhookContactsResponseBodyPageBeanWebhookContacts()
                self.webhook_contacts.append(temp_model.from_map(k))
        return self


class DescribeWebhookContactsResponseBody(TeaModel):
    def __init__(
        self,
        page_bean: DescribeWebhookContactsResponseBodyPageBean = None,
        request_id: str = None,
    ):
        # 分页对象
        self.page_bean = page_bean
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = DescribeWebhookContactsResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeWebhookContactsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeWebhookContactsResponseBody = None,
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
            temp_model = DescribeWebhookContactsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExploreTraceRequestAttributes(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        self.key = key
        self.operator = operator
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
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ExploreTraceRequest(TeaModel):
    def __init__(
        self,
        attributes: List[ExploreTraceRequestAttributes] = None,
        end_time: int = None,
        kind: str = None,
        max_duration: int = None,
        min_duration: int = None,
        page: int = None,
        page_size: int = None,
        region_id: str = None,
        selected_field: str = None,
        service_ip: str = None,
        service_name: str = None,
        span_name: str = None,
        start_time: int = None,
        status_code: str = None,
        trace_id: str = None,
    ):
        self.attributes = attributes
        self.end_time = end_time
        self.kind = kind
        self.max_duration = max_duration
        self.min_duration = min_duration
        self.page = page
        self.page_size = page_size
        self.region_id = region_id
        self.selected_field = selected_field
        self.service_ip = service_ip
        self.service_name = service_name
        self.span_name = span_name
        self.start_time = start_time
        self.status_code = status_code
        self.trace_id = trace_id

    def validate(self):
        if self.attributes:
            for k in self.attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Attributes'] = []
        if self.attributes is not None:
            for k in self.attributes:
                result['Attributes'].append(k.to_map() if k else None)
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.kind is not None:
            result['Kind'] = self.kind
        if self.max_duration is not None:
            result['MaxDuration'] = self.max_duration
        if self.min_duration is not None:
            result['MinDuration'] = self.min_duration
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.selected_field is not None:
            result['SelectedField'] = self.selected_field
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.span_name is not None:
            result['SpanName'] = self.span_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attributes = []
        if m.get('Attributes') is not None:
            for k in m.get('Attributes'):
                temp_model = ExploreTraceRequestAttributes()
                self.attributes.append(temp_model.from_map(k))
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        if m.get('MaxDuration') is not None:
            self.max_duration = m.get('MaxDuration')
        if m.get('MinDuration') is not None:
            self.min_duration = m.get('MinDuration')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SelectedField') is not None:
            self.selected_field = m.get('SelectedField')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SpanName') is not None:
            self.span_name = m.get('SpanName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ExploreTraceResponseBodySpanVOs(TeaModel):
    def __init__(
        self,
        attributes: Dict[str, str] = None,
        children: List[str] = None,
        duration: int = None,
        events: str = None,
        hidden_attributes: Dict[str, str] = None,
        hostname: str = None,
        ip: str = None,
        kind: str = None,
        labels: List[str] = None,
        links: str = None,
        meta: Dict[str, str] = None,
        parent_span_id: str = None,
        pid: str = None,
        resource: Dict[str, str] = None,
        sample_ids: str = None,
        service_name: str = None,
        span_id: str = None,
        span_name: str = None,
        start_time: int = None,
        status_code: int = None,
        status_message: str = None,
        trace_id: str = None,
    ):
        self.attributes = attributes
        self.children = children
        self.duration = duration
        self.events = events
        self.hidden_attributes = hidden_attributes
        self.hostname = hostname
        self.ip = ip
        self.kind = kind
        self.labels = labels
        self.links = links
        self.meta = meta
        self.parent_span_id = parent_span_id
        self.pid = pid
        self.resource = resource
        self.sample_ids = sample_ids
        self.service_name = service_name
        self.span_id = span_id
        self.span_name = span_name
        self.start_time = start_time
        self.status_code = status_code
        self.status_message = status_message
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.children is not None:
            result['Children'] = self.children
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.events is not None:
            result['Events'] = self.events
        if self.hidden_attributes is not None:
            result['HiddenAttributes'] = self.hidden_attributes
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.kind is not None:
            result['Kind'] = self.kind
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.links is not None:
            result['Links'] = self.links
        if self.meta is not None:
            result['Meta'] = self.meta
        if self.parent_span_id is not None:
            result['ParentSpanId'] = self.parent_span_id
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.sample_ids is not None:
            result['SampleIds'] = self.sample_ids
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.span_id is not None:
            result['SpanId'] = self.span_id
        if self.span_name is not None:
            result['SpanName'] = self.span_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Children') is not None:
            self.children = m.get('Children')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Events') is not None:
            self.events = m.get('Events')
        if m.get('HiddenAttributes') is not None:
            self.hidden_attributes = m.get('HiddenAttributes')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Links') is not None:
            self.links = m.get('Links')
        if m.get('Meta') is not None:
            self.meta = m.get('Meta')
        if m.get('ParentSpanId') is not None:
            self.parent_span_id = m.get('ParentSpanId')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('SampleIds') is not None:
            self.sample_ids = m.get('SampleIds')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SpanId') is not None:
            self.span_id = m.get('SpanId')
        if m.get('SpanName') is not None:
            self.span_name = m.get('SpanName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ExploreTraceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        span_vos: List[ExploreTraceResponseBodySpanVOs] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.span_vos = span_vos

    def validate(self):
        if self.span_vos:
            for k in self.span_vos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SpanVOs'] = []
        if self.span_vos is not None:
            for k in self.span_vos:
                result['SpanVOs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.span_vos = []
        if m.get('SpanVOs') is not None:
            for k in m.get('SpanVOs'):
                temp_model = ExploreTraceResponseBodySpanVOs()
                self.span_vos.append(temp_model.from_map(k))
        return self


class ExploreTraceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExploreTraceResponseBody = None,
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
            temp_model = ExploreTraceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetASMIntegrationStateRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetASMIntegrationStateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        state: bool = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class GetASMIntegrationStateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetASMIntegrationStateResponseBody = None,
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
            temp_model = GetASMIntegrationStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentDownloadUrlRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetAgentDownloadUrlResponseBody(TeaModel):
    def __init__(
        self,
        arms_agent_download_url: str = None,
        request_id: str = None,
    ):
        self.arms_agent_download_url = arms_agent_download_url
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arms_agent_download_url is not None:
            result['ArmsAgentDownloadUrl'] = self.arms_agent_download_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArmsAgentDownloadUrl') is not None:
            self.arms_agent_download_url = m.get('ArmsAgentDownloadUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAgentDownloadUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAgentDownloadUrlResponseBody = None,
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
            temp_model = GetAgentDownloadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlertRulesRequest(TeaModel):
    def __init__(
        self,
        alert_ids: str = None,
        alert_names: str = None,
        alert_status: str = None,
        alert_type: str = None,
        page: int = None,
        region_id: str = None,
        size: int = None,
    ):
        # 告警规则ID
        self.alert_ids = alert_ids
        # 告警规则名称
        self.alert_names = alert_names
        # 告警规则运行状态
        self.alert_status = alert_status
        # 告警规则类型
        self.alert_type = alert_type
        # 页数
        self.page = page
        # 地域
        self.region_id = region_id
        # 每一页大小
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_ids is not None:
            result['AlertIds'] = self.alert_ids
        if self.alert_names is not None:
            result['AlertNames'] = self.alert_names
        if self.alert_status is not None:
            result['AlertStatus'] = self.alert_status
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.page is not None:
            result['Page'] = self.page
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertIds') is not None:
            self.alert_ids = m.get('AlertIds')
        if m.get('AlertNames') is not None:
            self.alert_names = m.get('AlertNames')
        if m.get('AlertStatus') is not None:
            self.alert_status = m.get('AlertStatus')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class GetAlertRulesResponseBodyPageBeanAlertRulesAlertRuleContentAlertRuleItems(TeaModel):
    def __init__(
        self,
        aggregate: str = None,
        metric_key: str = None,
        n: float = None,
        operator: str = None,
        value: str = None,
    ):
        # 应用监控/前端监控-聚合方式
        self.aggregate = aggregate
        # 应用监控/前端监控-具体告警条件的指标
        self.metric_key = metric_key
        # 应用监控/前端监控-最近N分钟
        self.n = n
        # 应用监控/前端监控-判断条件
        self.operator = operator
        # 应用监控/前端监控-阈值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregate is not None:
            result['Aggregate'] = self.aggregate
        if self.metric_key is not None:
            result['MetricKey'] = self.metric_key
        if self.n is not None:
            result['N'] = self.n
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aggregate') is not None:
            self.aggregate = m.get('Aggregate')
        if m.get('MetricKey') is not None:
            self.metric_key = m.get('MetricKey')
        if m.get('N') is not None:
            self.n = m.get('N')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetAlertRulesResponseBodyPageBeanAlertRulesAlertRuleContent(TeaModel):
    def __init__(
        self,
        alert_rule_items: List[GetAlertRulesResponseBodyPageBeanAlertRulesAlertRuleContentAlertRuleItems] = None,
        condition: str = None,
    ):
        # 应用监控/前端监控-告警条件
        self.alert_rule_items = alert_rule_items
        # 应用监控/前端监控-多个告警条件触发逻辑
        self.condition = condition

    def validate(self):
        if self.alert_rule_items:
            for k in self.alert_rule_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlertRuleItems'] = []
        if self.alert_rule_items is not None:
            for k in self.alert_rule_items:
                result['AlertRuleItems'].append(k.to_map() if k else None)
        if self.condition is not None:
            result['Condition'] = self.condition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_rule_items = []
        if m.get('AlertRuleItems') is not None:
            for k in m.get('AlertRuleItems'):
                temp_model = GetAlertRulesResponseBodyPageBeanAlertRulesAlertRuleContentAlertRuleItems()
                self.alert_rule_items.append(temp_model.from_map(k))
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')
        return self


class GetAlertRulesResponseBodyPageBeanAlertRulesAnnotations(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # 键
        self.name = name
        # 值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetAlertRulesResponseBodyPageBeanAlertRulesFiltersCustomSLSFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        opt: str = None,
        show: bool = None,
        t: str = None,
        value: str = None,
    ):
        self.key = key
        self.opt = opt
        self.show = show
        self.t = t
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
        if self.opt is not None:
            result['Opt'] = self.opt
        if self.show is not None:
            result['Show'] = self.show
        if self.t is not None:
            result['T'] = self.t
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Opt') is not None:
            self.opt = m.get('Opt')
        if m.get('Show') is not None:
            self.show = m.get('Show')
        if m.get('T') is not None:
            self.t = m.get('T')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetAlertRulesResponseBodyPageBeanAlertRulesFiltersDimFilters(TeaModel):
    def __init__(
        self,
        filter_key: str = None,
        filter_opt: str = None,
        filter_values: List[str] = None,
    ):
        self.filter_key = filter_key
        self.filter_opt = filter_opt
        self.filter_values = filter_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key
        if self.filter_opt is not None:
            result['FilterOpt'] = self.filter_opt
        if self.filter_values is not None:
            result['FilterValues'] = self.filter_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')
        if m.get('FilterOpt') is not None:
            self.filter_opt = m.get('FilterOpt')
        if m.get('FilterValues') is not None:
            self.filter_values = m.get('FilterValues')
        return self


class GetAlertRulesResponseBodyPageBeanAlertRulesFilters(TeaModel):
    def __init__(
        self,
        custom_slsfilters: List[GetAlertRulesResponseBodyPageBeanAlertRulesFiltersCustomSLSFilters] = None,
        custom_slsgroup_by_dimensions: List[str] = None,
        custom_slswheres: List[str] = None,
        dim_filters: List[GetAlertRulesResponseBodyPageBeanAlertRulesFiltersDimFilters] = None,
    ):
        self.custom_slsfilters = custom_slsfilters
        self.custom_slsgroup_by_dimensions = custom_slsgroup_by_dimensions
        self.custom_slswheres = custom_slswheres
        self.dim_filters = dim_filters

    def validate(self):
        if self.custom_slsfilters:
            for k in self.custom_slsfilters:
                if k:
                    k.validate()
        if self.dim_filters:
            for k in self.dim_filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomSLSFilters'] = []
        if self.custom_slsfilters is not None:
            for k in self.custom_slsfilters:
                result['CustomSLSFilters'].append(k.to_map() if k else None)
        if self.custom_slsgroup_by_dimensions is not None:
            result['CustomSLSGroupByDimensions'] = self.custom_slsgroup_by_dimensions
        if self.custom_slswheres is not None:
            result['CustomSLSWheres'] = self.custom_slswheres
        result['DimFilters'] = []
        if self.dim_filters is not None:
            for k in self.dim_filters:
                result['DimFilters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_slsfilters = []
        if m.get('CustomSLSFilters') is not None:
            for k in m.get('CustomSLSFilters'):
                temp_model = GetAlertRulesResponseBodyPageBeanAlertRulesFiltersCustomSLSFilters()
                self.custom_slsfilters.append(temp_model.from_map(k))
        if m.get('CustomSLSGroupByDimensions') is not None:
            self.custom_slsgroup_by_dimensions = m.get('CustomSLSGroupByDimensions')
        if m.get('CustomSLSWheres') is not None:
            self.custom_slswheres = m.get('CustomSLSWheres')
        self.dim_filters = []
        if m.get('DimFilters') is not None:
            for k in m.get('DimFilters'):
                temp_model = GetAlertRulesResponseBodyPageBeanAlertRulesFiltersDimFilters()
                self.dim_filters.append(temp_model.from_map(k))
        return self


class GetAlertRulesResponseBodyPageBeanAlertRulesLabels(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # 键
        self.name = name
        # 值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetAlertRulesResponseBodyPageBeanAlertRules(TeaModel):
    def __init__(
        self,
        alert_check_type: str = None,
        alert_group: int = None,
        alert_id: float = None,
        alert_name: str = None,
        alert_rule_content: GetAlertRulesResponseBodyPageBeanAlertRulesAlertRuleContent = None,
        alert_status: str = None,
        alert_type: str = None,
        annotations: List[GetAlertRulesResponseBodyPageBeanAlertRulesAnnotations] = None,
        auto_add_new_application: bool = None,
        cluster_id: str = None,
        created_time: int = None,
        duration: str = None,
        extend: str = None,
        filters: GetAlertRulesResponseBodyPageBeanAlertRulesFilters = None,
        labels: List[GetAlertRulesResponseBodyPageBeanAlertRulesLabels] = None,
        level: str = None,
        message: str = None,
        metrics_type: str = None,
        notify_strategy: str = None,
        pids: List[str] = None,
        prom_ql: str = None,
        region_id: str = None,
        updated_time: int = None,
        user_id: str = None,
    ):
        # Prometheus告警-告警检查类型
        self.alert_check_type = alert_check_type
        # Prometheus告警-告警分组ID
        self.alert_group = alert_group
        # 告警规则ID
        self.alert_id = alert_id
        # 告警规则名称
        self.alert_name = alert_name
        # 应用监控/前端监控-告警规则内容
        self.alert_rule_content = alert_rule_content
        # 告警规则状态
        self.alert_status = alert_status
        # 告警规则类型
        self.alert_type = alert_type
        # Prometheus告警-Annotation
        self.annotations = annotations
        # 应用监控/前端监控-是否开启新创建应用追加到此告警规则
        self.auto_add_new_application = auto_add_new_application
        # Prometheus告警-集群ID
        self.cluster_id = cluster_id
        # 创建时间
        self.created_time = created_time
        # Prometheus告警-持续时间
        self.duration = duration
        # 扩展字段
        self.extend = extend
        # 应用监控/前端监控-告警条件-过滤项
        self.filters = filters
        # Prometheus告警-Label
        self.labels = labels
        # Prometheus告警-等级
        self.level = level
        # Prometheus告警-告警内容
        self.message = message
        # 应用监控/前端监控-告警指标类型
        self.metrics_type = metrics_type
        # 通知策略ID
        self.notify_strategy = notify_strategy
        # 应用监控/前端监控-告警关联应用ID
        self.pids = pids
        # Prometheus告警-PromQL语句
        self.prom_ql = prom_ql
        # 地域
        self.region_id = region_id
        # 更新时间
        self.updated_time = updated_time
        # 用户UID
        self.user_id = user_id

    def validate(self):
        if self.alert_rule_content:
            self.alert_rule_content.validate()
        if self.annotations:
            for k in self.annotations:
                if k:
                    k.validate()
        if self.filters:
            self.filters.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_check_type is not None:
            result['AlertCheckType'] = self.alert_check_type
        if self.alert_group is not None:
            result['AlertGroup'] = self.alert_group
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_rule_content is not None:
            result['AlertRuleContent'] = self.alert_rule_content.to_map()
        if self.alert_status is not None:
            result['AlertStatus'] = self.alert_status
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        result['Annotations'] = []
        if self.annotations is not None:
            for k in self.annotations:
                result['Annotations'].append(k.to_map() if k else None)
        if self.auto_add_new_application is not None:
            result['AutoAddNewApplication'] = self.auto_add_new_application
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.extend is not None:
            result['Extend'] = self.extend
        if self.filters is not None:
            result['Filters'] = self.filters.to_map()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.metrics_type is not None:
            result['MetricsType'] = self.metrics_type
        if self.notify_strategy is not None:
            result['NotifyStrategy'] = self.notify_strategy
        if self.pids is not None:
            result['Pids'] = self.pids
        if self.prom_ql is not None:
            result['PromQL'] = self.prom_ql
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertCheckType') is not None:
            self.alert_check_type = m.get('AlertCheckType')
        if m.get('AlertGroup') is not None:
            self.alert_group = m.get('AlertGroup')
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertRuleContent') is not None:
            temp_model = GetAlertRulesResponseBodyPageBeanAlertRulesAlertRuleContent()
            self.alert_rule_content = temp_model.from_map(m['AlertRuleContent'])
        if m.get('AlertStatus') is not None:
            self.alert_status = m.get('AlertStatus')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        self.annotations = []
        if m.get('Annotations') is not None:
            for k in m.get('Annotations'):
                temp_model = GetAlertRulesResponseBodyPageBeanAlertRulesAnnotations()
                self.annotations.append(temp_model.from_map(k))
        if m.get('AutoAddNewApplication') is not None:
            self.auto_add_new_application = m.get('AutoAddNewApplication')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Extend') is not None:
            self.extend = m.get('Extend')
        if m.get('Filters') is not None:
            temp_model = GetAlertRulesResponseBodyPageBeanAlertRulesFilters()
            self.filters = temp_model.from_map(m['Filters'])
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = GetAlertRulesResponseBodyPageBeanAlertRulesLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MetricsType') is not None:
            self.metrics_type = m.get('MetricsType')
        if m.get('NotifyStrategy') is not None:
            self.notify_strategy = m.get('NotifyStrategy')
        if m.get('Pids') is not None:
            self.pids = m.get('Pids')
        if m.get('PromQL') is not None:
            self.prom_ql = m.get('PromQL')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetAlertRulesResponseBodyPageBean(TeaModel):
    def __init__(
        self,
        alert_rules: List[GetAlertRulesResponseBodyPageBeanAlertRules] = None,
        page: int = None,
        size: int = None,
        total: int = None,
    ):
        # 告警规则列表
        self.alert_rules = alert_rules
        # 页数
        self.page = page
        # 每一页大小
        self.size = size
        # 总数
        self.total = total

    def validate(self):
        if self.alert_rules:
            for k in self.alert_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlertRules'] = []
        if self.alert_rules is not None:
            for k in self.alert_rules:
                result['AlertRules'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_rules = []
        if m.get('AlertRules') is not None:
            for k in m.get('AlertRules'):
                temp_model = GetAlertRulesResponseBodyPageBeanAlertRules()
                self.alert_rules.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetAlertRulesResponseBody(TeaModel):
    def __init__(
        self,
        page_bean: GetAlertRulesResponseBodyPageBean = None,
        request_id: str = None,
    ):
        # 分页对象
        self.page_bean = page_bean
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = GetAlertRulesResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAlertRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAlertRulesResponseBody = None,
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
            temp_model = GetAlertRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppApiByPageRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        end_time: int = None,
        interval_mills: int = None,
        pid: str = None,
        page_size: int = None,
        region_id: str = None,
        start_time: int = None,
    ):
        self.current_page = current_page
        self.end_time = end_time
        self.interval_mills = interval_mills
        self.pid = pid
        self.page_size = page_size
        self.region_id = region_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval_mills is not None:
            result['IntervalMills'] = self.interval_mills
        if self.pid is not None:
            result['PId'] = self.pid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IntervalMills') is not None:
            self.interval_mills = m.get('IntervalMills')
        if m.get('PId') is not None:
            self.pid = m.get('PId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetAppApiByPageResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[Dict[str, Any]] = None,
        page: int = None,
        page_size: int = None,
        total: str = None,
    ):
        self.items = items
        self.page = page
        self.page_size = page_size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            self.items = m.get('Items')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetAppApiByPageResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetAppApiByPageResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetAppApiByPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAppApiByPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAppApiByPageResponseBody = None,
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
            temp_model = GetAppApiByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetArmsAgentDownLoadUrlRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetArmsAgentDownLoadUrlResponseBody(TeaModel):
    def __init__(
        self,
        arms_agent_download_url: str = None,
        request_id: str = None,
    ):
        self.arms_agent_download_url = arms_agent_download_url
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arms_agent_download_url is not None:
            result['ArmsAgentDownloadUrl'] = self.arms_agent_download_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArmsAgentDownloadUrl') is not None:
            self.arms_agent_download_url = m.get('ArmsAgentDownloadUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetArmsAgentDownLoadUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetArmsAgentDownLoadUrlResponseBody = None,
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
            temp_model = GetArmsAgentDownLoadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuthTokenRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetAuthTokenResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
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


class GetAuthTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAuthTokenResponseBody = None,
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
            temp_model = GetAuthTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClusterInfoRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        query_user_id: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.query_user_id = query_user_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.query_user_id is not None:
            result['QueryUserId'] = self.query_user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('QueryUserId') is not None:
            self.query_user_id = m.get('QueryUserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetClusterInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        ack_not_running: bool = None,
        agent_helm_not_exist: bool = None,
        agent_service_not_exist: bool = None,
        arms_dbnot_exist: bool = None,
        check_type: str = None,
        get_cluster_info: str = None,
        have_agent_node_is_not_ready: bool = None,
        is_flink: bool = None,
        need_intervention: bool = None,
        need_retry: bool = None,
        node_size_is_zero: bool = None,
        pod_is_not_restart: bool = None,
    ):
        self.ack_not_running = ack_not_running
        self.agent_helm_not_exist = agent_helm_not_exist
        self.agent_service_not_exist = agent_service_not_exist
        self.arms_dbnot_exist = arms_dbnot_exist
        self.check_type = check_type
        self.get_cluster_info = get_cluster_info
        self.have_agent_node_is_not_ready = have_agent_node_is_not_ready
        self.is_flink = is_flink
        self.need_intervention = need_intervention
        self.need_retry = need_retry
        self.node_size_is_zero = node_size_is_zero
        self.pod_is_not_restart = pod_is_not_restart

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ack_not_running is not None:
            result['AckNotRunning'] = self.ack_not_running
        if self.agent_helm_not_exist is not None:
            result['AgentHelmNotExist'] = self.agent_helm_not_exist
        if self.agent_service_not_exist is not None:
            result['AgentServiceNotExist'] = self.agent_service_not_exist
        if self.arms_dbnot_exist is not None:
            result['ArmsDBNotExist'] = self.arms_dbnot_exist
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.get_cluster_info is not None:
            result['GetClusterInfo'] = self.get_cluster_info
        if self.have_agent_node_is_not_ready is not None:
            result['HaveAgentNodeIsNotReady'] = self.have_agent_node_is_not_ready
        if self.is_flink is not None:
            result['IsFlink'] = self.is_flink
        if self.need_intervention is not None:
            result['NeedIntervention'] = self.need_intervention
        if self.need_retry is not None:
            result['NeedRetry'] = self.need_retry
        if self.node_size_is_zero is not None:
            result['NodeSizeIsZero'] = self.node_size_is_zero
        if self.pod_is_not_restart is not None:
            result['PodIsNotRestart'] = self.pod_is_not_restart
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AckNotRunning') is not None:
            self.ack_not_running = m.get('AckNotRunning')
        if m.get('AgentHelmNotExist') is not None:
            self.agent_helm_not_exist = m.get('AgentHelmNotExist')
        if m.get('AgentServiceNotExist') is not None:
            self.agent_service_not_exist = m.get('AgentServiceNotExist')
        if m.get('ArmsDBNotExist') is not None:
            self.arms_dbnot_exist = m.get('ArmsDBNotExist')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('GetClusterInfo') is not None:
            self.get_cluster_info = m.get('GetClusterInfo')
        if m.get('HaveAgentNodeIsNotReady') is not None:
            self.have_agent_node_is_not_ready = m.get('HaveAgentNodeIsNotReady')
        if m.get('IsFlink') is not None:
            self.is_flink = m.get('IsFlink')
        if m.get('NeedIntervention') is not None:
            self.need_intervention = m.get('NeedIntervention')
        if m.get('NeedRetry') is not None:
            self.need_retry = m.get('NeedRetry')
        if m.get('NodeSizeIsZero') is not None:
            self.node_size_is_zero = m.get('NodeSizeIsZero')
        if m.get('PodIsNotRestart') is not None:
            self.pod_is_not_restart = m.get('PodIsNotRestart')
        return self


class GetClusterInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: GetClusterInfoResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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
            temp_model = GetClusterInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetClusterInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetClusterInfoResponseBody = None,
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
            temp_model = GetClusterInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClusterStateRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        puser_id: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.puser_id = puser_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.puser_id is not None:
            result['PuserId'] = self.puser_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PuserId') is not None:
            self.puser_id = m.get('PuserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetClusterStateResponseBodyResult(TeaModel):
    def __init__(
        self,
        agent_state: bool = None,
        cluster_state: str = None,
        is_flink: bool = None,
    ):
        self.agent_state = agent_state
        self.cluster_state = cluster_state
        self.is_flink = is_flink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_state is not None:
            result['agentState'] = self.agent_state
        if self.cluster_state is not None:
            result['clusterState'] = self.cluster_state
        if self.is_flink is not None:
            result['isFlink'] = self.is_flink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentState') is not None:
            self.agent_state = m.get('agentState')
        if m.get('clusterState') is not None:
            self.cluster_state = m.get('clusterState')
        if m.get('isFlink') is not None:
            self.is_flink = m.get('isFlink')
        return self


class GetClusterStateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetClusterStateResponseBodyResult = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.result = result

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
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('result') is not None:
            temp_model = GetClusterStateResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetClusterStateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetClusterStateResponseBody = None,
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
            temp_model = GetClusterStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEstimateFeeInfoRequest(TeaModel):
    def __init__(
        self,
        target_user_id: str = None,
        usage_cn: int = None,
        usage_fn: int = None,
    ):
        self.target_user_id = target_user_id
        self.usage_cn = usage_cn
        self.usage_fn = usage_fn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_user_id is not None:
            result['TargetUserId'] = self.target_user_id
        if self.usage_cn is not None:
            result['UsageCn'] = self.usage_cn
        if self.usage_fn is not None:
            result['UsageFn'] = self.usage_fn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetUserId') is not None:
            self.target_user_id = m.get('TargetUserId')
        if m.get('UsageCn') is not None:
            self.usage_cn = m.get('UsageCn')
        if m.get('UsageFn') is not None:
            self.usage_fn = m.get('UsageFn')
        return self


class GetEstimateFeeInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # data
        self.data = data
        # Id of the request
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


class GetEstimateFeeInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEstimateFeeInfoResponseBody = None,
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
            temp_model = GetEstimateFeeInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExploreUrlRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        expression: str = None,
        region_id: str = None,
        type: str = None,
    ):
        self.cluster_id = cluster_id
        self.expression = expression
        self.region_id = region_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetExploreUrlResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
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


class GetExploreUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExploreUrlResponseBody = None,
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
            temp_model = GetExploreUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIntegrationStateRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        integration: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.integration = integration
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.integration is not None:
            result['Integration'] = self.integration
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Integration') is not None:
            self.integration = m.get('Integration')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetIntegrationStateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        state: bool = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class GetIntegrationStateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetIntegrationStateResponseBody = None,
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
            temp_model = GetIntegrationStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMultipleTraceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        trace_ids: List[str] = None,
    ):
        self.region_id = region_id
        self.trace_ids = trace_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.trace_ids is not None:
            result['TraceIDs'] = self.trace_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TraceIDs') is not None:
            self.trace_ids = m.get('TraceIDs')
        return self


class GetMultipleTraceResponseBodyMultiCallChainInfosSpansLogEventListTagEntryList(TeaModel):
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


class GetMultipleTraceResponseBodyMultiCallChainInfosSpansLogEventList(TeaModel):
    def __init__(
        self,
        tag_entry_list: List[GetMultipleTraceResponseBodyMultiCallChainInfosSpansLogEventListTagEntryList] = None,
        timestamp: int = None,
    ):
        self.tag_entry_list = tag_entry_list
        self.timestamp = timestamp

    def validate(self):
        if self.tag_entry_list:
            for k in self.tag_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagEntryList'] = []
        if self.tag_entry_list is not None:
            for k in self.tag_entry_list:
                result['TagEntryList'].append(k.to_map() if k else None)
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_entry_list = []
        if m.get('TagEntryList') is not None:
            for k in m.get('TagEntryList'):
                temp_model = GetMultipleTraceResponseBodyMultiCallChainInfosSpansLogEventListTagEntryList()
                self.tag_entry_list.append(temp_model.from_map(k))
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetMultipleTraceResponseBodyMultiCallChainInfosSpansTagEntryList(TeaModel):
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


class GetMultipleTraceResponseBodyMultiCallChainInfosSpans(TeaModel):
    def __init__(
        self,
        duration: int = None,
        have_stack: bool = None,
        log_event_list: List[GetMultipleTraceResponseBodyMultiCallChainInfosSpansLogEventList] = None,
        operation_name: str = None,
        parent_span_id: str = None,
        result_code: str = None,
        rpc_id: str = None,
        rpc_type: int = None,
        service_ip: str = None,
        service_name: str = None,
        span_id: str = None,
        tag_entry_list: List[GetMultipleTraceResponseBodyMultiCallChainInfosSpansTagEntryList] = None,
        timestamp: int = None,
        trace_id: str = None,
    ):
        self.duration = duration
        self.have_stack = have_stack
        self.log_event_list = log_event_list
        self.operation_name = operation_name
        self.parent_span_id = parent_span_id
        self.result_code = result_code
        self.rpc_id = rpc_id
        self.rpc_type = rpc_type
        self.service_ip = service_ip
        self.service_name = service_name
        self.span_id = span_id
        self.tag_entry_list = tag_entry_list
        self.timestamp = timestamp
        self.trace_id = trace_id

    def validate(self):
        if self.log_event_list:
            for k in self.log_event_list:
                if k:
                    k.validate()
        if self.tag_entry_list:
            for k in self.tag_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.have_stack is not None:
            result['HaveStack'] = self.have_stack
        result['LogEventList'] = []
        if self.log_event_list is not None:
            for k in self.log_event_list:
                result['LogEventList'].append(k.to_map() if k else None)
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.parent_span_id is not None:
            result['ParentSpanId'] = self.parent_span_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.rpc_id is not None:
            result['RpcId'] = self.rpc_id
        if self.rpc_type is not None:
            result['RpcType'] = self.rpc_type
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.span_id is not None:
            result['SpanId'] = self.span_id
        result['TagEntryList'] = []
        if self.tag_entry_list is not None:
            for k in self.tag_entry_list:
                result['TagEntryList'].append(k.to_map() if k else None)
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('HaveStack') is not None:
            self.have_stack = m.get('HaveStack')
        self.log_event_list = []
        if m.get('LogEventList') is not None:
            for k in m.get('LogEventList'):
                temp_model = GetMultipleTraceResponseBodyMultiCallChainInfosSpansLogEventList()
                self.log_event_list.append(temp_model.from_map(k))
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('ParentSpanId') is not None:
            self.parent_span_id = m.get('ParentSpanId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('RpcId') is not None:
            self.rpc_id = m.get('RpcId')
        if m.get('RpcType') is not None:
            self.rpc_type = m.get('RpcType')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SpanId') is not None:
            self.span_id = m.get('SpanId')
        self.tag_entry_list = []
        if m.get('TagEntryList') is not None:
            for k in m.get('TagEntryList'):
                temp_model = GetMultipleTraceResponseBodyMultiCallChainInfosSpansTagEntryList()
                self.tag_entry_list.append(temp_model.from_map(k))
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class GetMultipleTraceResponseBodyMultiCallChainInfos(TeaModel):
    def __init__(
        self,
        spans: List[GetMultipleTraceResponseBodyMultiCallChainInfosSpans] = None,
        trace_id: str = None,
    ):
        self.spans = spans
        self.trace_id = trace_id

    def validate(self):
        if self.spans:
            for k in self.spans:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Spans'] = []
        if self.spans is not None:
            for k in self.spans:
                result['Spans'].append(k.to_map() if k else None)
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.spans = []
        if m.get('Spans') is not None:
            for k in m.get('Spans'):
                temp_model = GetMultipleTraceResponseBodyMultiCallChainInfosSpans()
                self.spans.append(temp_model.from_map(k))
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class GetMultipleTraceResponseBody(TeaModel):
    def __init__(
        self,
        multi_call_chain_infos: List[GetMultipleTraceResponseBodyMultiCallChainInfos] = None,
        request_id: str = None,
    ):
        self.multi_call_chain_infos = multi_call_chain_infos
        self.request_id = request_id

    def validate(self):
        if self.multi_call_chain_infos:
            for k in self.multi_call_chain_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MultiCallChainInfos'] = []
        if self.multi_call_chain_infos is not None:
            for k in self.multi_call_chain_infos:
                result['MultiCallChainInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.multi_call_chain_infos = []
        if m.get('MultiCallChainInfos') is not None:
            for k in m.get('MultiCallChainInfos'):
                temp_model = GetMultipleTraceResponseBodyMultiCallChainInfos()
                self.multi_call_chain_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMultipleTraceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMultipleTraceResponseBody = None,
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
            temp_model = GetMultipleTraceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPrometheusApiTokenRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetPrometheusApiTokenResponseBody(TeaModel):
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


class GetPrometheusApiTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPrometheusApiTokenResponseBody = None,
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
            temp_model = GetPrometheusApiTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPrometheusGlobalViewRequest(TeaModel):
    def __init__(
        self,
        global_view_cluster_id: str = None,
        region_id: str = None,
    ):
        self.global_view_cluster_id = global_view_cluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.global_view_cluster_id is not None:
            result['GlobalViewClusterId'] = self.global_view_cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GlobalViewClusterId') is not None:
            self.global_view_cluster_id = m.get('GlobalViewClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetPrometheusGlobalViewResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
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


class GetPrometheusGlobalViewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPrometheusGlobalViewResponseBody = None,
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
            temp_model = GetPrometheusGlobalViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRecordingRuleRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetRecordingRuleResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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


class GetRecordingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRecordingRuleResponseBody = None,
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
            temp_model = GetRecordingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRetcodeShareUrlRequest(TeaModel):
    def __init__(
        self,
        pid: str = None,
    ):
        self.pid = pid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pid is not None:
            result['Pid'] = self.pid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        return self


class GetRetcodeShareUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        url: str = None,
    ):
        self.request_id = request_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetRetcodeShareUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRetcodeShareUrlResponseBody = None,
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
            temp_model = GetRetcodeShareUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStackRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        pid: str = None,
        region_id: str = None,
        rpc_id: str = None,
        start_time: int = None,
        trace_id: str = None,
    ):
        self.end_time = end_time
        self.pid = pid
        self.region_id = region_id
        self.rpc_id = rpc_id
        self.start_time = start_time
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rpc_id is not None:
            result['RpcID'] = self.rpc_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RpcID') is not None:
            self.rpc_id = m.get('RpcID')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class GetStackResponseBodyStackInfoExtInfo(TeaModel):
    def __init__(
        self,
        info: str = None,
        type: str = None,
    ):
        self.info = info
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info is not None:
            result['Info'] = self.info
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Info') is not None:
            self.info = m.get('Info')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetStackResponseBodyStackInfo(TeaModel):
    def __init__(
        self,
        api: str = None,
        duration: int = None,
        exception: str = None,
        ext_info: GetStackResponseBodyStackInfoExtInfo = None,
        line: str = None,
        rpc_id: str = None,
        service_name: str = None,
        start_time: int = None,
    ):
        self.api = api
        self.duration = duration
        self.exception = exception
        self.ext_info = ext_info
        self.line = line
        self.rpc_id = rpc_id
        self.service_name = service_name
        self.start_time = start_time

    def validate(self):
        if self.ext_info:
            self.ext_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api is not None:
            result['Api'] = self.api
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.exception is not None:
            result['Exception'] = self.exception
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info.to_map()
        if self.line is not None:
            result['Line'] = self.line
        if self.rpc_id is not None:
            result['RpcId'] = self.rpc_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Api') is not None:
            self.api = m.get('Api')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Exception') is not None:
            self.exception = m.get('Exception')
        if m.get('ExtInfo') is not None:
            temp_model = GetStackResponseBodyStackInfoExtInfo()
            self.ext_info = temp_model.from_map(m['ExtInfo'])
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('RpcId') is not None:
            self.rpc_id = m.get('RpcId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetStackResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        stack_info: List[GetStackResponseBodyStackInfo] = None,
    ):
        self.request_id = request_id
        self.stack_info = stack_info

    def validate(self):
        if self.stack_info:
            for k in self.stack_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StackInfo'] = []
        if self.stack_info is not None:
            for k in self.stack_info:
                result['StackInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.stack_info = []
        if m.get('StackInfo') is not None:
            for k in m.get('StackInfo'):
                temp_model = GetStackResponseBodyStackInfo()
                self.stack_info.append(temp_model.from_map(k))
        return self


class GetStackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetStackResponseBody = None,
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
            temp_model = GetStackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTraceRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        region_id: str = None,
        start_time: int = None,
        trace_id: str = None,
    ):
        self.end_time = end_time
        self.region_id = region_id
        self.start_time = start_time
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class GetTraceResponseBodySpansLogEventListTagEntryList(TeaModel):
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


class GetTraceResponseBodySpansLogEventList(TeaModel):
    def __init__(
        self,
        tag_entry_list: List[GetTraceResponseBodySpansLogEventListTagEntryList] = None,
        timestamp: int = None,
    ):
        self.tag_entry_list = tag_entry_list
        self.timestamp = timestamp

    def validate(self):
        if self.tag_entry_list:
            for k in self.tag_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagEntryList'] = []
        if self.tag_entry_list is not None:
            for k in self.tag_entry_list:
                result['TagEntryList'].append(k.to_map() if k else None)
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_entry_list = []
        if m.get('TagEntryList') is not None:
            for k in m.get('TagEntryList'):
                temp_model = GetTraceResponseBodySpansLogEventListTagEntryList()
                self.tag_entry_list.append(temp_model.from_map(k))
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetTraceResponseBodySpansTagEntryList(TeaModel):
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


class GetTraceResponseBodySpans(TeaModel):
    def __init__(
        self,
        children: List[Dict[str, Any]] = None,
        duration: int = None,
        have_stack: bool = None,
        log_event_list: List[GetTraceResponseBodySpansLogEventList] = None,
        operation_name: str = None,
        parent_span_id: str = None,
        result_code: str = None,
        rpc_id: str = None,
        rpc_type: int = None,
        service_ip: str = None,
        service_name: str = None,
        span_id: str = None,
        tag_entry_list: List[GetTraceResponseBodySpansTagEntryList] = None,
        timestamp: int = None,
        trace_id: str = None,
    ):
        self.children = children
        self.duration = duration
        self.have_stack = have_stack
        self.log_event_list = log_event_list
        self.operation_name = operation_name
        self.parent_span_id = parent_span_id
        self.result_code = result_code
        self.rpc_id = rpc_id
        self.rpc_type = rpc_type
        self.service_ip = service_ip
        self.service_name = service_name
        self.span_id = span_id
        self.tag_entry_list = tag_entry_list
        self.timestamp = timestamp
        self.trace_id = trace_id

    def validate(self):
        if self.log_event_list:
            for k in self.log_event_list:
                if k:
                    k.validate()
        if self.tag_entry_list:
            for k in self.tag_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.children is not None:
            result['Children'] = self.children
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.have_stack is not None:
            result['HaveStack'] = self.have_stack
        result['LogEventList'] = []
        if self.log_event_list is not None:
            for k in self.log_event_list:
                result['LogEventList'].append(k.to_map() if k else None)
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.parent_span_id is not None:
            result['ParentSpanId'] = self.parent_span_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.rpc_id is not None:
            result['RpcId'] = self.rpc_id
        if self.rpc_type is not None:
            result['RpcType'] = self.rpc_type
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.span_id is not None:
            result['SpanId'] = self.span_id
        result['TagEntryList'] = []
        if self.tag_entry_list is not None:
            for k in self.tag_entry_list:
                result['TagEntryList'].append(k.to_map() if k else None)
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Children') is not None:
            self.children = m.get('Children')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('HaveStack') is not None:
            self.have_stack = m.get('HaveStack')
        self.log_event_list = []
        if m.get('LogEventList') is not None:
            for k in m.get('LogEventList'):
                temp_model = GetTraceResponseBodySpansLogEventList()
                self.log_event_list.append(temp_model.from_map(k))
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('ParentSpanId') is not None:
            self.parent_span_id = m.get('ParentSpanId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('RpcId') is not None:
            self.rpc_id = m.get('RpcId')
        if m.get('RpcType') is not None:
            self.rpc_type = m.get('RpcType')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SpanId') is not None:
            self.span_id = m.get('SpanId')
        self.tag_entry_list = []
        if m.get('TagEntryList') is not None:
            for k in m.get('TagEntryList'):
                temp_model = GetTraceResponseBodySpansTagEntryList()
                self.tag_entry_list.append(temp_model.from_map(k))
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class GetTraceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        spans: List[GetTraceResponseBodySpans] = None,
    ):
        self.request_id = request_id
        self.spans = spans

    def validate(self):
        if self.spans:
            for k in self.spans:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Spans'] = []
        if self.spans is not None:
            for k in self.spans:
                result['Spans'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.spans = []
        if m.get('Spans') is not None:
            for k in m.get('Spans'):
                temp_model = GetTraceResponseBodySpans()
                self.spans.append(temp_model.from_map(k))
        return self


class GetTraceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTraceResponseBody = None,
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
            temp_model = GetTraceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTraceAppRequest(TeaModel):
    def __init__(
        self,
        pid: str = None,
        region_id: str = None,
    ):
        self.pid = pid
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetTraceAppResponseBodyTraceApp(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        create_time: int = None,
        labels: List[str] = None,
        pid: str = None,
        region_id: str = None,
        show: bool = None,
        type: str = None,
        update_time: int = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.create_time = create_time
        self.labels = labels
        self.pid = pid
        self.region_id = region_id
        self.show = show
        self.type = type
        self.update_time = update_time
        self.user_id = user_id

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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.show is not None:
            result['Show'] = self.show
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Show') is not None:
            self.show = m.get('Show')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetTraceAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        trace_app: GetTraceAppResponseBodyTraceApp = None,
    ):
        self.request_id = request_id
        self.trace_app = trace_app

    def validate(self):
        if self.trace_app:
            self.trace_app.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_app is not None:
            result['TraceApp'] = self.trace_app.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceApp') is not None:
            temp_model = GetTraceAppResponseBodyTraceApp()
            self.trace_app = temp_model.from_map(m['TraceApp'])
        return self


class GetTraceAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTraceAppResponseBody = None,
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
            temp_model = GetTraceAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserCommercialStatusRequest(TeaModel):
    def __init__(
        self,
        parent_id: str = None,
        target_user_id: str = None,
        user_id: str = None,
    ):
        self.parent_id = parent_id
        self.target_user_id = target_user_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.target_user_id is not None:
            result['TargetUserId'] = self.target_user_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('TargetUserId') is not None:
            self.target_user_id = m.get('TargetUserId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetUserCommercialStatusResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
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


class GetUserCommercialStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserCommercialStatusResponseBody = None,
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
            temp_model = GetUserCommercialStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportAppAlertRulesRequest(TeaModel):
    def __init__(
        self,
        contact_group_ids: str = None,
        is_auto_start: bool = None,
        pids: str = None,
        region_id: str = None,
        templage_alert_config: str = None,
        template_alert_id: str = None,
    ):
        self.contact_group_ids = contact_group_ids
        self.is_auto_start = is_auto_start
        self.pids = pids
        self.region_id = region_id
        self.templage_alert_config = templage_alert_config
        self.template_alert_id = template_alert_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_ids is not None:
            result['ContactGroupIds'] = self.contact_group_ids
        if self.is_auto_start is not None:
            result['IsAutoStart'] = self.is_auto_start
        if self.pids is not None:
            result['Pids'] = self.pids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.templage_alert_config is not None:
            result['TemplageAlertConfig'] = self.templage_alert_config
        if self.template_alert_id is not None:
            result['TemplateAlertId'] = self.template_alert_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids = m.get('ContactGroupIds')
        if m.get('IsAutoStart') is not None:
            self.is_auto_start = m.get('IsAutoStart')
        if m.get('Pids') is not None:
            self.pids = m.get('Pids')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplageAlertConfig') is not None:
            self.templage_alert_config = m.get('TemplageAlertConfig')
        if m.get('TemplateAlertId') is not None:
            self.template_alert_id = m.get('TemplateAlertId')
        return self


class ImportAppAlertRulesResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
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


class ImportAppAlertRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImportAppAlertRulesResponseBody = None,
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
            temp_model = ImportAppAlertRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallCmsExporterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cms_args: str = None,
        enable_tag: bool = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.cms_args = cms_args
        self.enable_tag = enable_tag
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cms_args is not None:
            result['CmsArgs'] = self.cms_args
        if self.enable_tag is not None:
            result['EnableTag'] = self.enable_tag
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CmsArgs') is not None:
            self.cms_args = m.get('CmsArgs')
        if m.get('EnableTag') is not None:
            self.enable_tag = m.get('EnableTag')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class InstallCmsExporterResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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


class InstallCmsExporterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InstallCmsExporterResponseBody = None,
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
            temp_model = InstallCmsExporterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallManagedPrometheusRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_type: str = None,
        kube_config: str = None,
        region_id: str = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_type = cluster_type
        self.kube_config = kube_config
        self.region_id = region_id
        self.security_group_id = security_group_id
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.kube_config is not None:
            result['KubeConfig'] = self.kube_config
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('KubeConfig') is not None:
            self.kube_config = m.get('KubeConfig')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class InstallManagedPrometheusResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InstallManagedPrometheusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InstallManagedPrometheusResponseBody = None,
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
            temp_model = InstallManagedPrometheusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListActivatedAlertsRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        filter: str = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.current_page = current_page
        self.filter = filter
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListActivatedAlertsResponseBodyPageAlertsDispatchRules(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
        rule_name: str = None,
    ):
        self.rule_id = rule_id
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class ListActivatedAlertsResponseBodyPageAlerts(TeaModel):
    def __init__(
        self,
        alert_id: str = None,
        alert_name: str = None,
        alert_type: str = None,
        count: int = None,
        create_time: int = None,
        dispatch_rules: List[ListActivatedAlertsResponseBodyPageAlertsDispatchRules] = None,
        ends_at: int = None,
        expand_fields: Dict[str, Any] = None,
        integration_name: str = None,
        integration_type: str = None,
        involved_object_kind: str = None,
        involved_object_name: str = None,
        message: str = None,
        severity: str = None,
        starts_at: int = None,
        status: str = None,
    ):
        self.alert_id = alert_id
        self.alert_name = alert_name
        self.alert_type = alert_type
        self.count = count
        self.create_time = create_time
        self.dispatch_rules = dispatch_rules
        self.ends_at = ends_at
        self.expand_fields = expand_fields
        self.integration_name = integration_name
        self.integration_type = integration_type
        self.involved_object_kind = involved_object_kind
        self.involved_object_name = involved_object_name
        self.message = message
        self.severity = severity
        self.starts_at = starts_at
        self.status = status

    def validate(self):
        if self.dispatch_rules:
            for k in self.dispatch_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.count is not None:
            result['Count'] = self.count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['DispatchRules'] = []
        if self.dispatch_rules is not None:
            for k in self.dispatch_rules:
                result['DispatchRules'].append(k.to_map() if k else None)
        if self.ends_at is not None:
            result['EndsAt'] = self.ends_at
        if self.expand_fields is not None:
            result['ExpandFields'] = self.expand_fields
        if self.integration_name is not None:
            result['IntegrationName'] = self.integration_name
        if self.integration_type is not None:
            result['IntegrationType'] = self.integration_type
        if self.involved_object_kind is not None:
            result['InvolvedObjectKind'] = self.involved_object_kind
        if self.involved_object_name is not None:
            result['InvolvedObjectName'] = self.involved_object_name
        if self.message is not None:
            result['Message'] = self.message
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.starts_at is not None:
            result['StartsAt'] = self.starts_at
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.dispatch_rules = []
        if m.get('DispatchRules') is not None:
            for k in m.get('DispatchRules'):
                temp_model = ListActivatedAlertsResponseBodyPageAlertsDispatchRules()
                self.dispatch_rules.append(temp_model.from_map(k))
        if m.get('EndsAt') is not None:
            self.ends_at = m.get('EndsAt')
        if m.get('ExpandFields') is not None:
            self.expand_fields = m.get('ExpandFields')
        if m.get('IntegrationName') is not None:
            self.integration_name = m.get('IntegrationName')
        if m.get('IntegrationType') is not None:
            self.integration_type = m.get('IntegrationType')
        if m.get('InvolvedObjectKind') is not None:
            self.involved_object_kind = m.get('InvolvedObjectKind')
        if m.get('InvolvedObjectName') is not None:
            self.involved_object_name = m.get('InvolvedObjectName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('StartsAt') is not None:
            self.starts_at = m.get('StartsAt')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListActivatedAlertsResponseBodyPage(TeaModel):
    def __init__(
        self,
        alerts: List[ListActivatedAlertsResponseBodyPageAlerts] = None,
        page: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.alerts = alerts
        self.page = page
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.alerts:
            for k in self.alerts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Alerts'] = []
        if self.alerts is not None:
            for k in self.alerts:
                result['Alerts'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alerts = []
        if m.get('Alerts') is not None:
            for k in m.get('Alerts'):
                temp_model = ListActivatedAlertsResponseBodyPageAlerts()
                self.alerts.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListActivatedAlertsResponseBody(TeaModel):
    def __init__(
        self,
        page: ListActivatedAlertsResponseBodyPage = None,
        request_id: str = None,
    ):
        self.page = page
        self.request_id = request_id

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            temp_model = ListActivatedAlertsResponseBodyPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListActivatedAlertsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListActivatedAlertsResponseBody = None,
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
            temp_model = ListActivatedAlertsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlertsRequest(TeaModel):
    def __init__(
        self,
        alert_name: str = None,
        dispatch_rule_id: int = None,
        end_time: str = None,
        integration_type: str = None,
        page: int = None,
        severity: str = None,
        show_activities: bool = None,
        show_events: bool = None,
        size: int = None,
        start_time: str = None,
        state: int = None,
    ):
        # 告警名称
        self.alert_name = alert_name
        # 通知策略ID
        self.dispatch_rule_id = dispatch_rule_id
        # 查询告警发送历史记录的开始时间，时间格式：YYYY-MM-DD HH:mm:ss
        self.end_time = end_time
        # 集成类型
        self.integration_type = integration_type
        # 页数
        self.page = page
        # 告警等级(P1~P6)
        self.severity = severity
        # 默认不查活动记录，showActivities=true才查，只查最近3天的内容
        self.show_activities = show_activities
        # 默认不查事件，showEvents=true才查
        self.show_events = show_events
        # 每页展示数目
        self.size = size
        # 查询告警发送历史记录的开始时间，时间格式：YYYY-MM-DD HH:mm:ss
        self.start_time = start_time
        # 告警状态(0 - 待处理， 1 - 处理中， 2 - 已处理)
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.integration_type is not None:
            result['IntegrationType'] = self.integration_type
        if self.page is not None:
            result['Page'] = self.page
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.show_activities is not None:
            result['ShowActivities'] = self.show_activities
        if self.show_events is not None:
            result['ShowEvents'] = self.show_events
        if self.size is not None:
            result['Size'] = self.size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IntegrationType') is not None:
            self.integration_type = m.get('IntegrationType')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('ShowActivities') is not None:
            self.show_activities = m.get('ShowActivities')
        if m.get('ShowEvents') is not None:
            self.show_events = m.get('ShowEvents')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListAlertsResponseBodyPageBeanListAlertsActivities(TeaModel):
    def __init__(
        self,
        content: str = None,
        description: str = None,
        handler_name: str = None,
        time: str = None,
        type: int = None,
    ):
        # 通知内容
        self.content = content
        # 描述
        self.description = description
        # 处理人名称
        self.handler_name = handler_name
        # 时间
        self.time = time
        # 活动类型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.description is not None:
            result['Description'] = self.description
        if self.handler_name is not None:
            result['HandlerName'] = self.handler_name
        if self.time is not None:
            result['Time'] = self.time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HandlerName') is not None:
            self.handler_name = m.get('HandlerName')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListAlertsResponseBodyPageBeanListAlertsAlertEvents(TeaModel):
    def __init__(
        self,
        alert_name: str = None,
        annotations: str = None,
        description: str = None,
        end_time: str = None,
        generator_url: str = None,
        integration_name: str = None,
        integration_type: str = None,
        labels: str = None,
        receive_time: str = None,
        severity: str = None,
        start_time: str = None,
        state: str = None,
    ):
        # 事件名称
        self.alert_name = alert_name
        # 注释列表
        self.annotations = annotations
        # 事件描述
        self.description = description
        # 结束时间
        self.end_time = end_time
        # 事件地址
        self.generator_url = generator_url
        # 集成名称
        self.integration_name = integration_name
        # 集成类型
        self.integration_type = integration_type
        # 标签列表
        self.labels = labels
        # 事件接受时间
        self.receive_time = receive_time
        # 事件等级
        self.severity = severity
        # 开始时间
        self.start_time = start_time
        # 告警状态Active("Active"),      * Inhibited("Inhibited"),      * Silenced("Silenced"),      * Resolved("Resolved")
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.annotations is not None:
            result['Annotations'] = self.annotations
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.generator_url is not None:
            result['GeneratorURL'] = self.generator_url
        if self.integration_name is not None:
            result['IntegrationName'] = self.integration_name
        if self.integration_type is not None:
            result['IntegrationType'] = self.integration_type
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.receive_time is not None:
            result['ReceiveTime'] = self.receive_time
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GeneratorURL') is not None:
            self.generator_url = m.get('GeneratorURL')
        if m.get('IntegrationName') is not None:
            self.integration_name = m.get('IntegrationName')
        if m.get('IntegrationType') is not None:
            self.integration_type = m.get('IntegrationType')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('ReceiveTime') is not None:
            self.receive_time = m.get('ReceiveTime')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListAlertsResponseBodyPageBeanListAlerts(TeaModel):
    def __init__(
        self,
        activities: List[ListAlertsResponseBodyPageBeanListAlertsActivities] = None,
        alert_events: List[ListAlertsResponseBodyPageBeanListAlertsAlertEvents] = None,
        alert_id: int = None,
        alert_name: str = None,
        create_time: str = None,
        dispatch_rule_id: float = None,
        dispatch_rule_name: str = None,
        severity: str = None,
        state: int = None,
    ):
        # 活动列表
        self.activities = activities
        # 事件列表
        self.alert_events = alert_events
        # 告警ID
        self.alert_id = alert_id
        # 告警名称
        self.alert_name = alert_name
        # 创建时间
        self.create_time = create_time
        # 通知策略ID
        self.dispatch_rule_id = dispatch_rule_id
        # 通知策略名称
        self.dispatch_rule_name = dispatch_rule_name
        # 告警等级(P1~P6)
        self.severity = severity
        # 告警状态(0 - 待处理， 1 - 处理中， 2 - 已处理)
        self.state = state

    def validate(self):
        if self.activities:
            for k in self.activities:
                if k:
                    k.validate()
        if self.alert_events:
            for k in self.alert_events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Activities'] = []
        if self.activities is not None:
            for k in self.activities:
                result['Activities'].append(k.to_map() if k else None)
        result['AlertEvents'] = []
        if self.alert_events is not None:
            for k in self.alert_events:
                result['AlertEvents'].append(k.to_map() if k else None)
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id
        if self.dispatch_rule_name is not None:
            result['DispatchRuleName'] = self.dispatch_rule_name
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.activities = []
        if m.get('Activities') is not None:
            for k in m.get('Activities'):
                temp_model = ListAlertsResponseBodyPageBeanListAlertsActivities()
                self.activities.append(temp_model.from_map(k))
        self.alert_events = []
        if m.get('AlertEvents') is not None:
            for k in m.get('AlertEvents'):
                temp_model = ListAlertsResponseBodyPageBeanListAlertsAlertEvents()
                self.alert_events.append(temp_model.from_map(k))
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')
        if m.get('DispatchRuleName') is not None:
            self.dispatch_rule_name = m.get('DispatchRuleName')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListAlertsResponseBodyPageBean(TeaModel):
    def __init__(
        self,
        list_alerts: List[ListAlertsResponseBodyPageBeanListAlerts] = None,
        page: int = None,
        size: int = None,
        total: int = None,
    ):
        # 告警发送历史信息组
        self.list_alerts = list_alerts
        # 页数
        self.page = page
        # 每页展示数目
        self.size = size
        # 总数
        self.total = total

    def validate(self):
        if self.list_alerts:
            for k in self.list_alerts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ListAlerts'] = []
        if self.list_alerts is not None:
            for k in self.list_alerts:
                result['ListAlerts'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list_alerts = []
        if m.get('ListAlerts') is not None:
            for k in m.get('ListAlerts'):
                temp_model = ListAlertsResponseBodyPageBeanListAlerts()
                self.list_alerts.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListAlertsResponseBody(TeaModel):
    def __init__(
        self,
        page_bean: ListAlertsResponseBodyPageBean = None,
        request_id: str = None,
    ):
        # 返回结构体
        self.page_bean = page_bean
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = ListAlertsResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAlertsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAlertsResponseBody = None,
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
            temp_model = ListAlertsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterFromGrafanaRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListClusterFromGrafanaResponseBodyPromClusterList(TeaModel):
    def __init__(
        self,
        agent_status: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_type: str = None,
        controller_id: str = None,
        create_time: int = None,
        extra: str = None,
        id: int = None,
        install_time: int = None,
        is_controller_installed: bool = None,
        last_heart_beat_time: int = None,
        node_num: int = None,
        options: str = None,
        plugins_json_array: str = None,
        region_id: str = None,
        state_json: str = None,
        update_time: int = None,
        user_id: str = None,
    ):
        self.agent_status = agent_status
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.cluster_type = cluster_type
        self.controller_id = controller_id
        self.create_time = create_time
        self.extra = extra
        self.id = id
        self.install_time = install_time
        self.is_controller_installed = is_controller_installed
        self.last_heart_beat_time = last_heart_beat_time
        self.node_num = node_num
        self.options = options
        self.plugins_json_array = plugins_json_array
        self.region_id = region_id
        self.state_json = state_json
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.controller_id is not None:
            result['ControllerId'] = self.controller_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.id is not None:
            result['Id'] = self.id
        if self.install_time is not None:
            result['InstallTime'] = self.install_time
        if self.is_controller_installed is not None:
            result['IsControllerInstalled'] = self.is_controller_installed
        if self.last_heart_beat_time is not None:
            result['LastHeartBeatTime'] = self.last_heart_beat_time
        if self.node_num is not None:
            result['NodeNum'] = self.node_num
        if self.options is not None:
            result['Options'] = self.options
        if self.plugins_json_array is not None:
            result['PluginsJsonArray'] = self.plugins_json_array
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.state_json is not None:
            result['StateJson'] = self.state_json
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('ControllerId') is not None:
            self.controller_id = m.get('ControllerId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstallTime') is not None:
            self.install_time = m.get('InstallTime')
        if m.get('IsControllerInstalled') is not None:
            self.is_controller_installed = m.get('IsControllerInstalled')
        if m.get('LastHeartBeatTime') is not None:
            self.last_heart_beat_time = m.get('LastHeartBeatTime')
        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('PluginsJsonArray') is not None:
            self.plugins_json_array = m.get('PluginsJsonArray')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StateJson') is not None:
            self.state_json = m.get('StateJson')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListClusterFromGrafanaResponseBody(TeaModel):
    def __init__(
        self,
        prom_cluster_list: List[ListClusterFromGrafanaResponseBodyPromClusterList] = None,
        request_id: str = None,
    ):
        self.prom_cluster_list = prom_cluster_list
        self.request_id = request_id

    def validate(self):
        if self.prom_cluster_list:
            for k in self.prom_cluster_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PromClusterList'] = []
        if self.prom_cluster_list is not None:
            for k in self.prom_cluster_list:
                result['PromClusterList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.prom_cluster_list = []
        if m.get('PromClusterList') is not None:
            for k in m.get('PromClusterList'):
                temp_model = ListClusterFromGrafanaResponseBodyPromClusterList()
                self.prom_cluster_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListClusterFromGrafanaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListClusterFromGrafanaResponseBody = None,
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
            temp_model = ListClusterFromGrafanaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCmsInstancesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListCmsInstancesResponseBodyDataProducts(TeaModel):
    def __init__(
        self,
        descr: str = None,
        id: str = None,
        instance: str = None,
        name: str = None,
        prod: str = None,
        state: str = None,
        time: str = None,
        type: str = None,
        url: str = None,
    ):
        self.descr = descr
        self.id = id
        self.instance = instance
        self.name = name
        self.prod = prod
        self.state = state
        self.time = time
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.descr is not None:
            result['Descr'] = self.descr
        if self.id is not None:
            result['Id'] = self.id
        if self.instance is not None:
            result['Instance'] = self.instance
        if self.name is not None:
            result['Name'] = self.name
        if self.prod is not None:
            result['Prod'] = self.prod
        if self.state is not None:
            result['State'] = self.state
        if self.time is not None:
            result['Time'] = self.time
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Descr') is not None:
            self.descr = m.get('Descr')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Instance') is not None:
            self.instance = m.get('Instance')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Prod') is not None:
            self.prod = m.get('Prod')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListCmsInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        enable_tag: bool = None,
        products: List[ListCmsInstancesResponseBodyDataProducts] = None,
    ):
        self.enable_tag = enable_tag
        self.products = products

    def validate(self):
        if self.products:
            for k in self.products:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_tag is not None:
            result['EnableTag'] = self.enable_tag
        result['Products'] = []
        if self.products is not None:
            for k in self.products:
                result['Products'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableTag') is not None:
            self.enable_tag = m.get('EnableTag')
        self.products = []
        if m.get('Products') is not None:
            for k in m.get('Products'):
                temp_model = ListCmsInstancesResponseBodyDataProducts()
                self.products.append(temp_model.from_map(k))
        return self


class ListCmsInstancesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListCmsInstancesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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
            temp_model = ListCmsInstancesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListCmsInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCmsInstancesResponseBody = None,
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
            temp_model = ListCmsInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDashboardsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_type: str = None,
        dashboard_name: str = None,
        language: str = None,
        product: str = None,
        recreate_switch: bool = None,
        region_id: str = None,
        title: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_type = cluster_type
        self.dashboard_name = dashboard_name
        self.language = language
        self.product = product
        self.recreate_switch = recreate_switch
        self.region_id = region_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.dashboard_name is not None:
            result['DashboardName'] = self.dashboard_name
        if self.language is not None:
            result['Language'] = self.language
        if self.product is not None:
            result['Product'] = self.product
        if self.recreate_switch is not None:
            result['RecreateSwitch'] = self.recreate_switch
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('DashboardName') is not None:
            self.dashboard_name = m.get('DashboardName')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RecreateSwitch') is not None:
            self.recreate_switch = m.get('RecreateSwitch')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListDashboardsResponseBodyDashboardVosI18nChild(TeaModel):
    def __init__(
        self,
        dashboard_type: str = None,
        exporter: str = None,
        http_url: str = None,
        https_url: str = None,
        id: str = None,
        is_arms_exporter: bool = None,
        kind: str = None,
        language: str = None,
        name: str = None,
        need_update: bool = None,
        tags: List[str] = None,
        time: str = None,
        title: str = None,
        type: str = None,
        uid: str = None,
        url: str = None,
        version: str = None,
    ):
        self.dashboard_type = dashboard_type
        self.exporter = exporter
        self.http_url = http_url
        self.https_url = https_url
        self.id = id
        self.is_arms_exporter = is_arms_exporter
        self.kind = kind
        self.language = language
        self.name = name
        self.need_update = need_update
        self.tags = tags
        self.time = time
        self.title = title
        self.type = type
        self.uid = uid
        self.url = url
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dashboard_type is not None:
            result['DashboardType'] = self.dashboard_type
        if self.exporter is not None:
            result['Exporter'] = self.exporter
        if self.http_url is not None:
            result['HttpUrl'] = self.http_url
        if self.https_url is not None:
            result['HttpsUrl'] = self.https_url
        if self.id is not None:
            result['Id'] = self.id
        if self.is_arms_exporter is not None:
            result['IsArmsExporter'] = self.is_arms_exporter
        if self.kind is not None:
            result['Kind'] = self.kind
        if self.language is not None:
            result['Language'] = self.language
        if self.name is not None:
            result['Name'] = self.name
        if self.need_update is not None:
            result['NeedUpdate'] = self.need_update
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.time is not None:
            result['Time'] = self.time
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.url is not None:
            result['Url'] = self.url
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DashboardType') is not None:
            self.dashboard_type = m.get('DashboardType')
        if m.get('Exporter') is not None:
            self.exporter = m.get('Exporter')
        if m.get('HttpUrl') is not None:
            self.http_url = m.get('HttpUrl')
        if m.get('HttpsUrl') is not None:
            self.https_url = m.get('HttpsUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsArmsExporter') is not None:
            self.is_arms_exporter = m.get('IsArmsExporter')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NeedUpdate') is not None:
            self.need_update = m.get('NeedUpdate')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListDashboardsResponseBodyDashboardVos(TeaModel):
    def __init__(
        self,
        dashboard_type: str = None,
        exporter: str = None,
        http_url: str = None,
        https_url: str = None,
        i_18n_child: ListDashboardsResponseBodyDashboardVosI18nChild = None,
        id: str = None,
        is_arms_exporter: bool = None,
        kind: str = None,
        language: str = None,
        name: str = None,
        need_update: bool = None,
        tags: List[str] = None,
        time: str = None,
        title: str = None,
        type: str = None,
        uid: str = None,
        url: str = None,
        version: str = None,
    ):
        self.dashboard_type = dashboard_type
        self.exporter = exporter
        self.http_url = http_url
        self.https_url = https_url
        self.i_18n_child = i_18n_child
        self.id = id
        self.is_arms_exporter = is_arms_exporter
        self.kind = kind
        self.language = language
        self.name = name
        self.need_update = need_update
        self.tags = tags
        self.time = time
        self.title = title
        self.type = type
        self.uid = uid
        self.url = url
        self.version = version

    def validate(self):
        if self.i_18n_child:
            self.i_18n_child.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dashboard_type is not None:
            result['DashboardType'] = self.dashboard_type
        if self.exporter is not None:
            result['Exporter'] = self.exporter
        if self.http_url is not None:
            result['HttpUrl'] = self.http_url
        if self.https_url is not None:
            result['HttpsUrl'] = self.https_url
        if self.i_18n_child is not None:
            result['I18nChild'] = self.i_18n_child.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.is_arms_exporter is not None:
            result['IsArmsExporter'] = self.is_arms_exporter
        if self.kind is not None:
            result['Kind'] = self.kind
        if self.language is not None:
            result['Language'] = self.language
        if self.name is not None:
            result['Name'] = self.name
        if self.need_update is not None:
            result['NeedUpdate'] = self.need_update
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.time is not None:
            result['Time'] = self.time
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.url is not None:
            result['Url'] = self.url
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DashboardType') is not None:
            self.dashboard_type = m.get('DashboardType')
        if m.get('Exporter') is not None:
            self.exporter = m.get('Exporter')
        if m.get('HttpUrl') is not None:
            self.http_url = m.get('HttpUrl')
        if m.get('HttpsUrl') is not None:
            self.https_url = m.get('HttpsUrl')
        if m.get('I18nChild') is not None:
            temp_model = ListDashboardsResponseBodyDashboardVosI18nChild()
            self.i_18n_child = temp_model.from_map(m['I18nChild'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsArmsExporter') is not None:
            self.is_arms_exporter = m.get('IsArmsExporter')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NeedUpdate') is not None:
            self.need_update = m.get('NeedUpdate')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListDashboardsResponseBody(TeaModel):
    def __init__(
        self,
        dashboard_vos: List[ListDashboardsResponseBodyDashboardVos] = None,
        request_id: str = None,
    ):
        self.dashboard_vos = dashboard_vos
        self.request_id = request_id

    def validate(self):
        if self.dashboard_vos:
            for k in self.dashboard_vos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DashboardVos'] = []
        if self.dashboard_vos is not None:
            for k in self.dashboard_vos:
                result['DashboardVos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dashboard_vos = []
        if m.get('DashboardVos') is not None:
            for k in m.get('DashboardVos'):
                temp_model = ListDashboardsResponseBodyDashboardVos()
                self.dashboard_vos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDashboardsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDashboardsResponseBody = None,
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
            temp_model = ListDashboardsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDispatchRuleRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        region_id: str = None,
        system: bool = None,
    ):
        self.name = name
        self.region_id = region_id
        self.system = system

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.system is not None:
            result['System'] = self.system
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('System') is not None:
            self.system = m.get('System')
        return self


class ListDispatchRuleResponseBodyDispatchRules(TeaModel):
    def __init__(
        self,
        name: str = None,
        rule_id: int = None,
        state: str = None,
    ):
        self.name = name
        self.rule_id = rule_id
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListDispatchRuleResponseBody(TeaModel):
    def __init__(
        self,
        dispatch_rules: List[ListDispatchRuleResponseBodyDispatchRules] = None,
        request_id: str = None,
    ):
        self.dispatch_rules = dispatch_rules
        self.request_id = request_id

    def validate(self):
        if self.dispatch_rules:
            for k in self.dispatch_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DispatchRules'] = []
        if self.dispatch_rules is not None:
            for k in self.dispatch_rules:
                result['DispatchRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dispatch_rules = []
        if m.get('DispatchRules') is not None:
            for k in m.get('DispatchRules'):
                temp_model = ListDispatchRuleResponseBodyDispatchRules()
                self.dispatch_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDispatchRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDispatchRuleResponseBody = None,
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
            temp_model = ListDispatchRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEscalationPoliciesRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page: int = None,
        size: int = None,
    ):
        self.name = name
        # 页数
        self.page = page
        # 每页展示数目
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListEscalationPoliciesResponseBodyPageBeanEscalationPolicies(TeaModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListEscalationPoliciesResponseBodyPageBean(TeaModel):
    def __init__(
        self,
        escalation_policies: List[ListEscalationPoliciesResponseBodyPageBeanEscalationPolicies] = None,
        page: int = None,
        size: int = None,
        total: int = None,
    ):
        self.escalation_policies = escalation_policies
        # 页数
        self.page = page
        # 每页展示数目
        self.size = size
        # 总数
        self.total = total

    def validate(self):
        if self.escalation_policies:
            for k in self.escalation_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EscalationPolicies'] = []
        if self.escalation_policies is not None:
            for k in self.escalation_policies:
                result['EscalationPolicies'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.escalation_policies = []
        if m.get('EscalationPolicies') is not None:
            for k in m.get('EscalationPolicies'):
                temp_model = ListEscalationPoliciesResponseBodyPageBeanEscalationPolicies()
                self.escalation_policies.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListEscalationPoliciesResponseBody(TeaModel):
    def __init__(
        self,
        page_bean: ListEscalationPoliciesResponseBodyPageBean = None,
        request_id: str = None,
    ):
        # 分页对象
        self.page_bean = page_bean
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = ListEscalationPoliciesResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListEscalationPoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEscalationPoliciesResponseBody = None,
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
            temp_model = ListEscalationPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEventBridgeIntegrationsRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page: int = None,
        size: int = None,
    ):
        self.name = name
        self.page = page
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListEventBridgeIntegrationsResponseBodyPageBeanEventBridgeIntegrations(TeaModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        name: str = None,
    ):
        self.description = description
        self.id = id
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
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListEventBridgeIntegrationsResponseBodyPageBean(TeaModel):
    def __init__(
        self,
        event_bridge_integrations: List[ListEventBridgeIntegrationsResponseBodyPageBeanEventBridgeIntegrations] = None,
        page: int = None,
        size: int = None,
        total: int = None,
    ):
        self.event_bridge_integrations = event_bridge_integrations
        self.page = page
        self.size = size
        self.total = total

    def validate(self):
        if self.event_bridge_integrations:
            for k in self.event_bridge_integrations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventBridgeIntegrations'] = []
        if self.event_bridge_integrations is not None:
            for k in self.event_bridge_integrations:
                result['EventBridgeIntegrations'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_bridge_integrations = []
        if m.get('EventBridgeIntegrations') is not None:
            for k in m.get('EventBridgeIntegrations'):
                temp_model = ListEventBridgeIntegrationsResponseBodyPageBeanEventBridgeIntegrations()
                self.event_bridge_integrations.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListEventBridgeIntegrationsResponseBody(TeaModel):
    def __init__(
        self,
        page_bean: ListEventBridgeIntegrationsResponseBodyPageBean = None,
        request_id: str = None,
    ):
        self.page_bean = page_bean
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = ListEventBridgeIntegrationsResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListEventBridgeIntegrationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEventBridgeIntegrationsResponseBody = None,
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
            temp_model = ListEventBridgeIntegrationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNotificationPoliciesRequest(TeaModel):
    def __init__(
        self,
        is_detail: bool = None,
        name: str = None,
        page: int = None,
        size: int = None,
    ):
        # 是否查询详情信息
        self.is_detail = is_detail
        # 通知策略名称
        self.name = name
        # 页数
        self.page = page
        # 每页展示数目
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_detail is not None:
            result['IsDetail'] = self.is_detail
        if self.name is not None:
            result['Name'] = self.name
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDetail') is not None:
            self.is_detail = m.get('IsDetail')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesGroupRule(TeaModel):
    def __init__(
        self,
        group_interval: int = None,
        group_wait: int = None,
        grouping_fields: List[str] = None,
    ):
        # 分组间隔时间，选填，默认是30s
        self.group_interval = group_interval
        # 分组等待时间，选填，默认是5秒
        self.group_wait = group_wait
        # 分组字段,为空则不分组，默认按照alertname分组
        self.grouping_fields = grouping_fields

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_interval is not None:
            result['GroupInterval'] = self.group_interval
        if self.group_wait is not None:
            result['GroupWait'] = self.group_wait
        if self.grouping_fields is not None:
            result['GroupingFields'] = self.grouping_fields
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupInterval') is not None:
            self.group_interval = m.get('GroupInterval')
        if m.get('GroupWait') is not None:
            self.group_wait = m.get('GroupWait')
        if m.get('GroupingFields') is not None:
            self.grouping_fields = m.get('GroupingFields')
        return self


class ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesMatchingRulesMatchingConditions(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # 条件字段
        self.key = key
        # 对应关系
        self.operator = operator
        # 条件字段值
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
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesMatchingRules(TeaModel):
    def __init__(
        self,
        matching_conditions: List[ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesMatchingRulesMatchingConditions] = None,
    ):
        # 匹配条件
        self.matching_conditions = matching_conditions

    def validate(self):
        if self.matching_conditions:
            for k in self.matching_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MatchingConditions'] = []
        if self.matching_conditions is not None:
            for k in self.matching_conditions:
                result['MatchingConditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.matching_conditions = []
        if m.get('MatchingConditions') is not None:
            for k in m.get('MatchingConditions'):
                temp_model = ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesMatchingRulesMatchingConditions()
                self.matching_conditions.append(temp_model.from_map(k))
        return self


class ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesNotifyRuleNotifyObjects(TeaModel):
    def __init__(
        self,
        notify_object_id: int = None,
        notify_object_name: str = None,
        notify_object_type: str = None,
    ):
        # 通知对象ID
        self.notify_object_id = notify_object_id
        # 通知对象名称
        self.notify_object_name = notify_object_name
        # 通知对象类型，CONTACT, CONTACT_GROUP, ARMS_CONTACT, DING_ROBOT
        self.notify_object_type = notify_object_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify_object_id is not None:
            result['NotifyObjectId'] = self.notify_object_id
        if self.notify_object_name is not None:
            result['NotifyObjectName'] = self.notify_object_name
        if self.notify_object_type is not None:
            result['NotifyObjectType'] = self.notify_object_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotifyObjectId') is not None:
            self.notify_object_id = m.get('NotifyObjectId')
        if m.get('NotifyObjectName') is not None:
            self.notify_object_name = m.get('NotifyObjectName')
        if m.get('NotifyObjectType') is not None:
            self.notify_object_type = m.get('NotifyObjectType')
        return self


class ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesNotifyRule(TeaModel):
    def __init__(
        self,
        notify_channels: List[str] = None,
        notify_end_time: str = None,
        notify_objects: List[ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesNotifyRuleNotifyObjects] = None,
        notify_start_time: str = None,
    ):
        # 通知渠道
        self.notify_channels = notify_channels
        # 通知时间段结束时间
        self.notify_end_time = notify_end_time
        # 通知对象
        self.notify_objects = notify_objects
        # 通知时间段开始时间
        self.notify_start_time = notify_start_time

    def validate(self):
        if self.notify_objects:
            for k in self.notify_objects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify_channels is not None:
            result['NotifyChannels'] = self.notify_channels
        if self.notify_end_time is not None:
            result['NotifyEndTime'] = self.notify_end_time
        result['NotifyObjects'] = []
        if self.notify_objects is not None:
            for k in self.notify_objects:
                result['NotifyObjects'].append(k.to_map() if k else None)
        if self.notify_start_time is not None:
            result['NotifyStartTime'] = self.notify_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotifyChannels') is not None:
            self.notify_channels = m.get('NotifyChannels')
        if m.get('NotifyEndTime') is not None:
            self.notify_end_time = m.get('NotifyEndTime')
        self.notify_objects = []
        if m.get('NotifyObjects') is not None:
            for k in m.get('NotifyObjects'):
                temp_model = ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesNotifyRuleNotifyObjects()
                self.notify_objects.append(temp_model.from_map(k))
        if m.get('NotifyStartTime') is not None:
            self.notify_start_time = m.get('NotifyStartTime')
        return self


class ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesNotifyTemplate(TeaModel):
    def __init__(
        self,
        email_content: str = None,
        email_recover_content: str = None,
        email_recover_title: str = None,
        email_title: str = None,
        robot_content: str = None,
        sms_content: str = None,
        sms_recover_content: str = None,
        tts_content: str = None,
        tts_recover_content: str = None,
    ):
        # 邮件内容
        self.email_content = email_content
        # 恢复告警邮件内容
        self.email_recover_content = email_recover_content
        # 恢复告警邮件标题
        self.email_recover_title = email_recover_title
        # 邮件标题
        self.email_title = email_title
        # 机器人告警内容
        self.robot_content = robot_content
        # 短信内容
        self.sms_content = sms_content
        # 恢复告警短信内容
        self.sms_recover_content = sms_recover_content
        # 智能语音告警内容
        self.tts_content = tts_content
        # 智能语音恢复告警内容
        self.tts_recover_content = tts_recover_content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email_content is not None:
            result['EmailContent'] = self.email_content
        if self.email_recover_content is not None:
            result['EmailRecoverContent'] = self.email_recover_content
        if self.email_recover_title is not None:
            result['EmailRecoverTitle'] = self.email_recover_title
        if self.email_title is not None:
            result['EmailTitle'] = self.email_title
        if self.robot_content is not None:
            result['RobotContent'] = self.robot_content
        if self.sms_content is not None:
            result['SmsContent'] = self.sms_content
        if self.sms_recover_content is not None:
            result['SmsRecoverContent'] = self.sms_recover_content
        if self.tts_content is not None:
            result['TtsContent'] = self.tts_content
        if self.tts_recover_content is not None:
            result['TtsRecoverContent'] = self.tts_recover_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmailContent') is not None:
            self.email_content = m.get('EmailContent')
        if m.get('EmailRecoverContent') is not None:
            self.email_recover_content = m.get('EmailRecoverContent')
        if m.get('EmailRecoverTitle') is not None:
            self.email_recover_title = m.get('EmailRecoverTitle')
        if m.get('EmailTitle') is not None:
            self.email_title = m.get('EmailTitle')
        if m.get('RobotContent') is not None:
            self.robot_content = m.get('RobotContent')
        if m.get('SmsContent') is not None:
            self.sms_content = m.get('SmsContent')
        if m.get('SmsRecoverContent') is not None:
            self.sms_recover_content = m.get('SmsRecoverContent')
        if m.get('TtsContent') is not None:
            self.tts_content = m.get('TtsContent')
        if m.get('TtsRecoverContent') is not None:
            self.tts_recover_content = m.get('TtsRecoverContent')
        return self


class ListNotificationPoliciesResponseBodyPageBeanNotificationPolicies(TeaModel):
    def __init__(
        self,
        escalation_policy_id: int = None,
        group_rule: ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesGroupRule = None,
        id: int = None,
        integration_id: int = None,
        matching_rules: List[ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesMatchingRules] = None,
        name: str = None,
        notify_rule: ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesNotifyRule = None,
        notify_template: ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesNotifyTemplate = None,
        repeat: bool = None,
        repeat_interval: int = None,
        send_recover_message: bool = None,
    ):
        # 升级规则ID
        self.escalation_policy_id = escalation_policy_id
        # 分组规则
        self.group_rule = group_rule
        # 通知策略ID
        self.id = id
        # 集成ID
        self.integration_id = integration_id
        # 事件匹配规则列表
        self.matching_rules = matching_rules
        # 通知策略名称
        self.name = name
        # 通知规则
        self.notify_rule = notify_rule
        # 通知模板
        self.notify_template = notify_template
        # 是否重复通知
        self.repeat = repeat
        # 重复通知时间间隔
        self.repeat_interval = repeat_interval
        # 是否发送恢复通知
        self.send_recover_message = send_recover_message

    def validate(self):
        if self.group_rule:
            self.group_rule.validate()
        if self.matching_rules:
            for k in self.matching_rules:
                if k:
                    k.validate()
        if self.notify_rule:
            self.notify_rule.validate()
        if self.notify_template:
            self.notify_template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.escalation_policy_id is not None:
            result['EscalationPolicyId'] = self.escalation_policy_id
        if self.group_rule is not None:
            result['GroupRule'] = self.group_rule.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.integration_id is not None:
            result['IntegrationId'] = self.integration_id
        result['MatchingRules'] = []
        if self.matching_rules is not None:
            for k in self.matching_rules:
                result['MatchingRules'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.notify_rule is not None:
            result['NotifyRule'] = self.notify_rule.to_map()
        if self.notify_template is not None:
            result['NotifyTemplate'] = self.notify_template.to_map()
        if self.repeat is not None:
            result['Repeat'] = self.repeat
        if self.repeat_interval is not None:
            result['RepeatInterval'] = self.repeat_interval
        if self.send_recover_message is not None:
            result['SendRecoverMessage'] = self.send_recover_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EscalationPolicyId') is not None:
            self.escalation_policy_id = m.get('EscalationPolicyId')
        if m.get('GroupRule') is not None:
            temp_model = ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesGroupRule()
            self.group_rule = temp_model.from_map(m['GroupRule'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IntegrationId') is not None:
            self.integration_id = m.get('IntegrationId')
        self.matching_rules = []
        if m.get('MatchingRules') is not None:
            for k in m.get('MatchingRules'):
                temp_model = ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesMatchingRules()
                self.matching_rules.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NotifyRule') is not None:
            temp_model = ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesNotifyRule()
            self.notify_rule = temp_model.from_map(m['NotifyRule'])
        if m.get('NotifyTemplate') is not None:
            temp_model = ListNotificationPoliciesResponseBodyPageBeanNotificationPoliciesNotifyTemplate()
            self.notify_template = temp_model.from_map(m['NotifyTemplate'])
        if m.get('Repeat') is not None:
            self.repeat = m.get('Repeat')
        if m.get('RepeatInterval') is not None:
            self.repeat_interval = m.get('RepeatInterval')
        if m.get('SendRecoverMessage') is not None:
            self.send_recover_message = m.get('SendRecoverMessage')
        return self


class ListNotificationPoliciesResponseBodyPageBean(TeaModel):
    def __init__(
        self,
        notification_policies: List[ListNotificationPoliciesResponseBodyPageBeanNotificationPolicies] = None,
        page: int = None,
        size: int = None,
        total: int = None,
    ):
        # 通知策略对象
        self.notification_policies = notification_policies
        # 页数
        self.page = page
        # 每页展示数目
        self.size = size
        # 总数
        self.total = total

    def validate(self):
        if self.notification_policies:
            for k in self.notification_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NotificationPolicies'] = []
        if self.notification_policies is not None:
            for k in self.notification_policies:
                result['NotificationPolicies'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.notification_policies = []
        if m.get('NotificationPolicies') is not None:
            for k in m.get('NotificationPolicies'):
                temp_model = ListNotificationPoliciesResponseBodyPageBeanNotificationPolicies()
                self.notification_policies.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListNotificationPoliciesResponseBody(TeaModel):
    def __init__(
        self,
        page_bean: ListNotificationPoliciesResponseBodyPageBean = None,
        request_id: str = None,
    ):
        # 分页对象
        self.page_bean = page_bean
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = ListNotificationPoliciesResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListNotificationPoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNotificationPoliciesResponseBody = None,
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
            temp_model = ListNotificationPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOnCallSchedulesRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page: int = None,
        size: int = None,
    ):
        # 排班策略名称
        self.name = name
        # 页数
        self.page = page
        # 展示数目
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListOnCallSchedulesResponseBodyPageBeanOnCallSchedules(TeaModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        name: str = None,
    ):
        # 排班策略描述
        self.description = description
        # 排班策略ID
        self.id = id
        # 排班策略名称
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
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListOnCallSchedulesResponseBodyPageBean(TeaModel):
    def __init__(
        self,
        on_call_schedules: List[ListOnCallSchedulesResponseBodyPageBeanOnCallSchedules] = None,
        page: int = None,
        size: int = None,
        total: int = None,
    ):
        self.on_call_schedules = on_call_schedules
        # 页数
        self.page = page
        # 每页展示数目
        self.size = size
        # 总数
        self.total = total

    def validate(self):
        if self.on_call_schedules:
            for k in self.on_call_schedules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OnCallSchedules'] = []
        if self.on_call_schedules is not None:
            for k in self.on_call_schedules:
                result['OnCallSchedules'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.on_call_schedules = []
        if m.get('OnCallSchedules') is not None:
            for k in m.get('OnCallSchedules'):
                temp_model = ListOnCallSchedulesResponseBodyPageBeanOnCallSchedules()
                self.on_call_schedules.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListOnCallSchedulesResponseBody(TeaModel):
    def __init__(
        self,
        page_bean: ListOnCallSchedulesResponseBodyPageBean = None,
        request_id: str = None,
    ):
        # 分页对象
        self.page_bean = page_bean
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = ListOnCallSchedulesResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListOnCallSchedulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOnCallSchedulesResponseBody = None,
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
            temp_model = ListOnCallSchedulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPrometheusAlertRulesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        match_expressions: str = None,
        name: str = None,
        region_id: str = None,
        status: int = None,
        type: str = None,
    ):
        self.cluster_id = cluster_id
        self.match_expressions = match_expressions
        self.name = name
        self.region_id = region_id
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.match_expressions is not None:
            result['MatchExpressions'] = self.match_expressions
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('MatchExpressions') is not None:
            self.match_expressions = m.get('MatchExpressions')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesAnnotations(TeaModel):
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
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesLabels(TeaModel):
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
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListPrometheusAlertRulesResponseBodyPrometheusAlertRules(TeaModel):
    def __init__(
        self,
        alert_id: int = None,
        alert_name: str = None,
        annotations: List[ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesAnnotations] = None,
        cluster_id: str = None,
        dispatch_rule_id: int = None,
        duration: str = None,
        expression: str = None,
        labels: List[ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesLabels] = None,
        message: str = None,
        notify_type: str = None,
        status: int = None,
        type: str = None,
    ):
        self.alert_id = alert_id
        self.alert_name = alert_name
        self.annotations = annotations
        self.cluster_id = cluster_id
        self.dispatch_rule_id = dispatch_rule_id
        self.duration = duration
        self.expression = expression
        self.labels = labels
        self.message = message
        self.notify_type = notify_type
        self.status = status
        self.type = type

    def validate(self):
        if self.annotations:
            for k in self.annotations:
                if k:
                    k.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        result['Annotations'] = []
        if self.annotations is not None:
            for k in self.annotations:
                result['Annotations'].append(k.to_map() if k else None)
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expression is not None:
            result['Expression'] = self.expression
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        self.annotations = []
        if m.get('Annotations') is not None:
            for k in m.get('Annotations'):
                temp_model = ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesAnnotations()
                self.annotations.append(temp_model.from_map(k))
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ListPrometheusAlertRulesResponseBodyPrometheusAlertRulesLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListPrometheusAlertRulesResponseBody(TeaModel):
    def __init__(
        self,
        prometheus_alert_rules: List[ListPrometheusAlertRulesResponseBodyPrometheusAlertRules] = None,
        request_id: str = None,
    ):
        self.prometheus_alert_rules = prometheus_alert_rules
        self.request_id = request_id

    def validate(self):
        if self.prometheus_alert_rules:
            for k in self.prometheus_alert_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PrometheusAlertRules'] = []
        if self.prometheus_alert_rules is not None:
            for k in self.prometheus_alert_rules:
                result['PrometheusAlertRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.prometheus_alert_rules = []
        if m.get('PrometheusAlertRules') is not None:
            for k in m.get('PrometheusAlertRules'):
                temp_model = ListPrometheusAlertRulesResponseBodyPrometheusAlertRules()
                self.prometheus_alert_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPrometheusAlertRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPrometheusAlertRulesResponseBody = None,
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
            temp_model = ListPrometheusAlertRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPrometheusAlertTemplatesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplatesAnnotations(TeaModel):
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
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplatesLabels(TeaModel):
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
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplates(TeaModel):
    def __init__(
        self,
        alert_name: str = None,
        annotations: List[ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplatesAnnotations] = None,
        description: str = None,
        duration: str = None,
        expression: str = None,
        labels: List[ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplatesLabels] = None,
        type: str = None,
        version: str = None,
    ):
        self.alert_name = alert_name
        self.annotations = annotations
        self.description = description
        self.duration = duration
        self.expression = expression
        self.labels = labels
        self.type = type
        self.version = version

    def validate(self):
        if self.annotations:
            for k in self.annotations:
                if k:
                    k.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        result['Annotations'] = []
        if self.annotations is not None:
            for k in self.annotations:
                result['Annotations'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expression is not None:
            result['Expression'] = self.expression
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        self.annotations = []
        if m.get('Annotations') is not None:
            for k in m.get('Annotations'):
                temp_model = ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplatesAnnotations()
                self.annotations.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplatesLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListPrometheusAlertTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        prometheus_alert_templates: List[ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplates] = None,
        request_id: str = None,
    ):
        self.prometheus_alert_templates = prometheus_alert_templates
        self.request_id = request_id

    def validate(self):
        if self.prometheus_alert_templates:
            for k in self.prometheus_alert_templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PrometheusAlertTemplates'] = []
        if self.prometheus_alert_templates is not None:
            for k in self.prometheus_alert_templates:
                result['PrometheusAlertTemplates'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.prometheus_alert_templates = []
        if m.get('PrometheusAlertTemplates') is not None:
            for k in m.get('PrometheusAlertTemplates'):
                temp_model = ListPrometheusAlertTemplatesResponseBodyPrometheusAlertTemplates()
                self.prometheus_alert_templates.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPrometheusAlertTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPrometheusAlertTemplatesResponseBody = None,
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
            temp_model = ListPrometheusAlertTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPrometheusGlobalViewRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListPrometheusGlobalViewResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
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


class ListPrometheusGlobalViewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPrometheusGlobalViewResponseBody = None,
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
            temp_model = ListPrometheusGlobalViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRetcodeAppsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        security_token: str = None,
    ):
        self.region_id = region_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ListRetcodeAppsResponseBodyRetcodeApps(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        pid: str = None,
        retcode_app_type: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.pid = pid
        self.retcode_app_type = retcode_app_type

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
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.retcode_app_type is not None:
            result['RetcodeAppType'] = self.retcode_app_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RetcodeAppType') is not None:
            self.retcode_app_type = m.get('RetcodeAppType')
        return self


class ListRetcodeAppsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        retcode_apps: List[ListRetcodeAppsResponseBodyRetcodeApps] = None,
    ):
        self.request_id = request_id
        self.retcode_apps = retcode_apps

    def validate(self):
        if self.retcode_apps:
            for k in self.retcode_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RetcodeApps'] = []
        if self.retcode_apps is not None:
            for k in self.retcode_apps:
                result['RetcodeApps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.retcode_apps = []
        if m.get('RetcodeApps') is not None:
            for k in m.get('RetcodeApps'):
                temp_model = ListRetcodeAppsResponseBodyRetcodeApps()
                self.retcode_apps.append(temp_model.from_map(k))
        return self


class ListRetcodeAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRetcodeAppsResponseBody = None,
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
            temp_model = ListRetcodeAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListScenarioRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        name: str = None,
        region_id: str = None,
        scenario: str = None,
        sign: str = None,
    ):
        self.app_id = app_id
        self.name = name
        self.region_id = region_id
        self.scenario = scenario
        self.sign = sign

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scenario is not None:
            result['Scenario'] = self.scenario
        if self.sign is not None:
            result['Sign'] = self.sign
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        return self


class ListScenarioResponseBodyArmsScenarios(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        create_time: str = None,
        extensions: str = None,
        id: int = None,
        name: str = None,
        region_id: str = None,
        sign: str = None,
        update_time: str = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.create_time = create_time
        self.extensions = extensions
        self.id = id
        self.name = name
        self.region_id = region_id
        self.sign = sign
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListScenarioResponseBody(TeaModel):
    def __init__(
        self,
        arms_scenarios: List[ListScenarioResponseBodyArmsScenarios] = None,
        request_id: str = None,
    ):
        self.arms_scenarios = arms_scenarios
        self.request_id = request_id

    def validate(self):
        if self.arms_scenarios:
            for k in self.arms_scenarios:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ArmsScenarios'] = []
        if self.arms_scenarios is not None:
            for k in self.arms_scenarios:
                result['ArmsScenarios'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.arms_scenarios = []
        if m.get('ArmsScenarios') is not None:
            for k in m.get('ArmsScenarios'):
                temp_model = ListScenarioResponseBodyArmsScenarios()
                self.arms_scenarios.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListScenarioResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListScenarioResponseBody = None,
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
            temp_model = ListScenarioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSilencePoliciesRequest(TeaModel):
    def __init__(
        self,
        is_detail: bool = None,
        name: str = None,
        page: int = None,
        size: int = None,
    ):
        # 是否查询详情信息
        self.is_detail = is_detail
        # 静默策略名称
        self.name = name
        # 页数
        self.page = page
        # 每页战术数目
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_detail is not None:
            result['IsDetail'] = self.is_detail
        if self.name is not None:
            result['Name'] = self.name
        if self.page is not None:
            result['Page'] = self.page
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDetail') is not None:
            self.is_detail = m.get('IsDetail')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListSilencePoliciesResponseBodyPageBeanSilencePoliciesMatchingRulesMatchingConditions(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # 条件字段
        self.key = key
        # 对应关系
        self.operator = operator
        # 条件字段值
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
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListSilencePoliciesResponseBodyPageBeanSilencePoliciesMatchingRules(TeaModel):
    def __init__(
        self,
        matching_conditions: List[ListSilencePoliciesResponseBodyPageBeanSilencePoliciesMatchingRulesMatchingConditions] = None,
    ):
        # 匹配条件
        self.matching_conditions = matching_conditions

    def validate(self):
        if self.matching_conditions:
            for k in self.matching_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MatchingConditions'] = []
        if self.matching_conditions is not None:
            for k in self.matching_conditions:
                result['MatchingConditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.matching_conditions = []
        if m.get('MatchingConditions') is not None:
            for k in m.get('MatchingConditions'):
                temp_model = ListSilencePoliciesResponseBodyPageBeanSilencePoliciesMatchingRulesMatchingConditions()
                self.matching_conditions.append(temp_model.from_map(k))
        return self


class ListSilencePoliciesResponseBodyPageBeanSilencePolicies(TeaModel):
    def __init__(
        self,
        id: int = None,
        matching_rules: List[ListSilencePoliciesResponseBodyPageBeanSilencePoliciesMatchingRules] = None,
        name: str = None,
    ):
        # 静默策略ID
        self.id = id
        # 事件匹配规则列表
        self.matching_rules = matching_rules
        # 静默策略名称
        self.name = name

    def validate(self):
        if self.matching_rules:
            for k in self.matching_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        result['MatchingRules'] = []
        if self.matching_rules is not None:
            for k in self.matching_rules:
                result['MatchingRules'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.matching_rules = []
        if m.get('MatchingRules') is not None:
            for k in m.get('MatchingRules'):
                temp_model = ListSilencePoliciesResponseBodyPageBeanSilencePoliciesMatchingRules()
                self.matching_rules.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListSilencePoliciesResponseBodyPageBean(TeaModel):
    def __init__(
        self,
        page: int = None,
        silence_policies: List[ListSilencePoliciesResponseBodyPageBeanSilencePolicies] = None,
        size: int = None,
        total: int = None,
    ):
        # 页数
        self.page = page
        # 静默策略列表
        self.silence_policies = silence_policies
        # 每页数目
        self.size = size
        # 总数
        self.total = total

    def validate(self):
        if self.silence_policies:
            for k in self.silence_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        result['SilencePolicies'] = []
        if self.silence_policies is not None:
            for k in self.silence_policies:
                result['SilencePolicies'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        self.silence_policies = []
        if m.get('SilencePolicies') is not None:
            for k in m.get('SilencePolicies'):
                temp_model = ListSilencePoliciesResponseBodyPageBeanSilencePolicies()
                self.silence_policies.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListSilencePoliciesResponseBody(TeaModel):
    def __init__(
        self,
        page_bean: ListSilencePoliciesResponseBodyPageBean = None,
        request_id: str = None,
    ):
        # 分页对象
        self.page_bean = page_bean
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = ListSilencePoliciesResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSilencePoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSilencePoliciesResponseBody = None,
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
            temp_model = ListSilencePoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.next_token = next_token
        self.resource_id = resource_id
        self.resource_type = resource_type
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


class ListTagResourcesResponseBodyTagResources(TeaModel):
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


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # TagResource
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
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTraceAppsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListTraceAppsResponseBodyTraceApps(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        create_time: int = None,
        labels: List[str] = None,
        pid: str = None,
        region_id: str = None,
        show: bool = None,
        type: str = None,
        update_time: int = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.create_time = create_time
        self.labels = labels
        self.pid = pid
        self.region_id = region_id
        self.show = show
        self.type = type
        self.update_time = update_time
        self.user_id = user_id

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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.show is not None:
            result['Show'] = self.show
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Show') is not None:
            self.show = m.get('Show')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListTraceAppsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_apps: List[ListTraceAppsResponseBodyTraceApps] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_apps = trace_apps

    def validate(self):
        if self.trace_apps:
            for k in self.trace_apps:
                if k:
                    k.validate()

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
        if self.success is not None:
            result['Success'] = self.success
        result['TraceApps'] = []
        if self.trace_apps is not None:
            for k in self.trace_apps:
                result['TraceApps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.trace_apps = []
        if m.get('TraceApps') is not None:
            for k in m.get('TraceApps'):
                temp_model = ListTraceAppsResponseBodyTraceApps()
                self.trace_apps.append(temp_model.from_map(k))
        return self


class ListTraceAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTraceAppsResponseBody = None,
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
            temp_model = ListTraceAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ManageGetRecordingRuleRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        query_user_id: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.query_user_id = query_user_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.query_user_id is not None:
            result['QueryUserId'] = self.query_user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('QueryUserId') is not None:
            self.query_user_id = m.get('QueryUserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ManageGetRecordingRuleResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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


class ManageGetRecordingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ManageGetRecordingRuleResponseBody = None,
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
            temp_model = ManageGetRecordingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ManageRecordingRuleRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        query_user_id: str = None,
        region_id: str = None,
        rule_yaml: str = None,
    ):
        self.cluster_id = cluster_id
        self.query_user_id = query_user_id
        self.region_id = region_id
        self.rule_yaml = rule_yaml

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.query_user_id is not None:
            result['QueryUserId'] = self.query_user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_yaml is not None:
            result['RuleYaml'] = self.rule_yaml
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('QueryUserId') is not None:
            self.query_user_id = m.get('QueryUserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleYaml') is not None:
            self.rule_yaml = m.get('RuleYaml')
        return self


class ManageRecordingRuleResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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


class ManageRecordingRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ManageRecordingRuleResponseBody = None,
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
            temp_model = ManageRecordingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenArmsDefaultSLRRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class OpenArmsDefaultSLRResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
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


class OpenArmsDefaultSLRResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenArmsDefaultSLRResponseBody = None,
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
            temp_model = OpenArmsDefaultSLRResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenArmsServiceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        type: str = None,
    ):
        self.owner_id = owner_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class OpenArmsServiceResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenArmsServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenArmsServiceResponseBody = None,
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
            temp_model = OpenArmsServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenArmsServiceSecondVersionRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        type: str = None,
    ):
        self.region_id = region_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class OpenArmsServiceSecondVersionResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenArmsServiceSecondVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenArmsServiceSecondVersionResponseBody = None,
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
            temp_model = OpenArmsServiceSecondVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenVClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_type: str = None,
        length: int = None,
        product: str = None,
        recreate_switch: bool = None,
        region_id: str = None,
    ):
        self.cluster_type = cluster_type
        self.length = length
        self.product = product
        self.recreate_switch = recreate_switch
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.length is not None:
            result['Length'] = self.length
        if self.product is not None:
            result['Product'] = self.product
        if self.recreate_switch is not None:
            result['RecreateSwitch'] = self.recreate_switch
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Length') is not None:
            self.length = m.get('Length')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RecreateSwitch') is not None:
            self.recreate_switch = m.get('RecreateSwitch')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class OpenVClusterResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
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


class OpenVClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenVClusterResponseBody = None,
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
            temp_model = OpenVClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenXtraceDefaultSLRRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class OpenXtraceDefaultSLRResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
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


class OpenXtraceDefaultSLRResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenXtraceDefaultSLRResponseBody = None,
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
            temp_model = OpenXtraceDefaultSLRResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PromVpcExporterManagerRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        exporter_config: str = None,
        exporter_type: str = None,
        method: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.exporter_config = exporter_config
        self.exporter_type = exporter_type
        self.method = method
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.exporter_config is not None:
            result['ExporterConfig'] = self.exporter_config
        if self.exporter_type is not None:
            result['ExporterType'] = self.exporter_type
        if self.method is not None:
            result['Method'] = self.method
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ExporterConfig') is not None:
            self.exporter_config = m.get('ExporterConfig')
        if m.get('ExporterType') is not None:
            self.exporter_type = m.get('ExporterType')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class PromVpcExporterManagerResponseBody(TeaModel):
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


class PromVpcExporterManagerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PromVpcExporterManagerResponseBody = None,
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
            temp_model = PromVpcExporterManagerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDatasetRequestDimensions(TeaModel):
    def __init__(
        self,
        key: str = None,
        type: str = None,
        value: str = None,
    ):
        self.key = key
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
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryDatasetRequestOptionalDims(TeaModel):
    def __init__(
        self,
        key: str = None,
        type: str = None,
        value: str = None,
    ):
        self.key = key
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
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryDatasetRequestRequiredDims(TeaModel):
    def __init__(
        self,
        key: str = None,
        type: str = None,
        value: str = None,
    ):
        self.key = key
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
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryDatasetRequest(TeaModel):
    def __init__(
        self,
        dataset_id: int = None,
        date_str: str = None,
        dimensions: List[QueryDatasetRequestDimensions] = None,
        hungry_mode: bool = None,
        interval_in_sec: int = None,
        is_drill_down: bool = None,
        limit: int = None,
        max_time: int = None,
        measures: List[str] = None,
        min_time: int = None,
        optional_dims: List[QueryDatasetRequestOptionalDims] = None,
        order_by_key: str = None,
        proxy_user_id: str = None,
        reduce_tail: bool = None,
        required_dims: List[QueryDatasetRequestRequiredDims] = None,
    ):
        self.dataset_id = dataset_id
        self.date_str = date_str
        self.dimensions = dimensions
        self.hungry_mode = hungry_mode
        self.interval_in_sec = interval_in_sec
        self.is_drill_down = is_drill_down
        self.limit = limit
        self.max_time = max_time
        self.measures = measures
        self.min_time = min_time
        self.optional_dims = optional_dims
        self.order_by_key = order_by_key
        self.proxy_user_id = proxy_user_id
        self.reduce_tail = reduce_tail
        self.required_dims = required_dims

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()
        if self.optional_dims:
            for k in self.optional_dims:
                if k:
                    k.validate()
        if self.required_dims:
            for k in self.required_dims:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.date_str is not None:
            result['DateStr'] = self.date_str
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.hungry_mode is not None:
            result['HungryMode'] = self.hungry_mode
        if self.interval_in_sec is not None:
            result['IntervalInSec'] = self.interval_in_sec
        if self.is_drill_down is not None:
            result['IsDrillDown'] = self.is_drill_down
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.max_time is not None:
            result['MaxTime'] = self.max_time
        if self.measures is not None:
            result['Measures'] = self.measures
        if self.min_time is not None:
            result['MinTime'] = self.min_time
        result['OptionalDims'] = []
        if self.optional_dims is not None:
            for k in self.optional_dims:
                result['OptionalDims'].append(k.to_map() if k else None)
        if self.order_by_key is not None:
            result['OrderByKey'] = self.order_by_key
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.reduce_tail is not None:
            result['ReduceTail'] = self.reduce_tail
        result['RequiredDims'] = []
        if self.required_dims is not None:
            for k in self.required_dims:
                result['RequiredDims'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DateStr') is not None:
            self.date_str = m.get('DateStr')
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = QueryDatasetRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('HungryMode') is not None:
            self.hungry_mode = m.get('HungryMode')
        if m.get('IntervalInSec') is not None:
            self.interval_in_sec = m.get('IntervalInSec')
        if m.get('IsDrillDown') is not None:
            self.is_drill_down = m.get('IsDrillDown')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('MaxTime') is not None:
            self.max_time = m.get('MaxTime')
        if m.get('Measures') is not None:
            self.measures = m.get('Measures')
        if m.get('MinTime') is not None:
            self.min_time = m.get('MinTime')
        self.optional_dims = []
        if m.get('OptionalDims') is not None:
            for k in m.get('OptionalDims'):
                temp_model = QueryDatasetRequestOptionalDims()
                self.optional_dims.append(temp_model.from_map(k))
        if m.get('OrderByKey') is not None:
            self.order_by_key = m.get('OrderByKey')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('ReduceTail') is not None:
            self.reduce_tail = m.get('ReduceTail')
        self.required_dims = []
        if m.get('RequiredDims') is not None:
            for k in m.get('RequiredDims'):
                temp_model = QueryDatasetRequestRequiredDims()
                self.required_dims.append(temp_model.from_map(k))
        return self


class QueryDatasetResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
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


class QueryDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDatasetResponseBody = None,
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
            temp_model = QueryDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMetricByPageRequestFilters(TeaModel):
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


class QueryMetricByPageRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        custom_filters: List[str] = None,
        dimensions: List[str] = None,
        end_time: int = None,
        filters: List[QueryMetricByPageRequestFilters] = None,
        interval_in_sec: int = None,
        measures: List[str] = None,
        metric: str = None,
        order: str = None,
        order_by: str = None,
        page_size: int = None,
        start_time: int = None,
    ):
        self.current_page = current_page
        self.custom_filters = custom_filters
        self.dimensions = dimensions
        self.end_time = end_time
        self.filters = filters
        self.interval_in_sec = interval_in_sec
        self.measures = measures
        self.metric = metric
        self.order = order
        self.order_by = order_by
        self.page_size = page_size
        self.start_time = start_time

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.custom_filters is not None:
            result['CustomFilters'] = self.custom_filters
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.interval_in_sec is not None:
            result['IntervalInSec'] = self.interval_in_sec
        if self.measures is not None:
            result['Measures'] = self.measures
        if self.metric is not None:
            result['Metric'] = self.metric
        if self.order is not None:
            result['Order'] = self.order
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('CustomFilters') is not None:
            self.custom_filters = m.get('CustomFilters')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = QueryMetricByPageRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('IntervalInSec') is not None:
            self.interval_in_sec = m.get('IntervalInSec')
        if m.get('Measures') is not None:
            self.measures = m.get('Measures')
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryMetricByPageResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[Dict[str, Any]] = None,
        page: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.items = items
        self.page = page
        self.page_size = page_size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            self.items = m.get('Items')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryMetricByPageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryMetricByPageResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryMetricByPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMetricByPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMetricByPageResponseBody = None,
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
            temp_model = QueryMetricByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPromInstallStatusRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class QueryPromInstallStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        is_controller_installed: bool = None,
    ):
        self.is_controller_installed = is_controller_installed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_controller_installed is not None:
            result['isControllerInstalled'] = self.is_controller_installed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isControllerInstalled') is not None:
            self.is_controller_installed = m.get('isControllerInstalled')
        return self


class QueryPromInstallStatusResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryPromInstallStatusResponseBodyData = None,
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
            temp_model = QueryPromInstallStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryPromInstallStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPromInstallStatusResponseBody = None,
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
            temp_model = QueryPromInstallStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryReleaseMetricRequest(TeaModel):
    def __init__(
        self,
        change_order_id: str = None,
        create_time: int = None,
        metric_type: str = None,
        pid: str = None,
        proxy_user_id: str = None,
        release_end_time: int = None,
        release_start_time: int = None,
        service: str = None,
    ):
        self.change_order_id = change_order_id
        self.create_time = create_time
        self.metric_type = metric_type
        self.pid = pid
        self.proxy_user_id = proxy_user_id
        self.release_end_time = release_end_time
        self.release_start_time = release_start_time
        self.service = service

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.release_end_time is not None:
            result['ReleaseEndTime'] = self.release_end_time
        if self.release_start_time is not None:
            result['ReleaseStartTime'] = self.release_start_time
        if self.service is not None:
            result['Service'] = self.service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('ReleaseEndTime') is not None:
            self.release_end_time = m.get('ReleaseEndTime')
        if m.get('ReleaseStartTime') is not None:
            self.release_start_time = m.get('ReleaseStartTime')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        return self


class QueryReleaseMetricResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
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


class QueryReleaseMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryReleaseMetricResponseBody = None,
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
            temp_model = QueryReleaseMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTracesRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        region_id: str = None,
        start_time: int = None,
        trace_id: str = None,
    ):
        self.end_time = end_time
        self.region_id = region_id
        self.start_time = start_time
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class QueryTracesResponseBodyTraceLists(TeaModel):
    def __init__(
        self,
        attributes: Dict[str, str] = None,
        duration: int = None,
        events: str = None,
        hidden_attributes: Dict[str, str] = None,
        hostname: str = None,
        ip: str = None,
        kind: str = None,
        links: str = None,
        parent_span_id: str = None,
        pid: str = None,
        resources: Dict[str, str] = None,
        sample_ids: str = None,
        service_name: int = None,
        span_id: str = None,
        span_name: str = None,
        start_time: int = None,
        status_code: int = None,
        status_message: str = None,
        trace_id: str = None,
    ):
        self.attributes = attributes
        self.duration = duration
        self.events = events
        self.hidden_attributes = hidden_attributes
        self.hostname = hostname
        self.ip = ip
        self.kind = kind
        self.links = links
        self.parent_span_id = parent_span_id
        self.pid = pid
        self.resources = resources
        self.sample_ids = sample_ids
        self.service_name = service_name
        self.span_id = span_id
        self.span_name = span_name
        self.start_time = start_time
        self.status_code = status_code
        self.status_message = status_message
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.events is not None:
            result['Events'] = self.events
        if self.hidden_attributes is not None:
            result['HiddenAttributes'] = self.hidden_attributes
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.kind is not None:
            result['Kind'] = self.kind
        if self.links is not None:
            result['Links'] = self.links
        if self.parent_span_id is not None:
            result['ParentSpanId'] = self.parent_span_id
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.sample_ids is not None:
            result['SampleIds'] = self.sample_ids
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.span_id is not None:
            result['SpanId'] = self.span_id
        if self.span_name is not None:
            result['SpanName'] = self.span_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Events') is not None:
            self.events = m.get('Events')
        if m.get('HiddenAttributes') is not None:
            self.hidden_attributes = m.get('HiddenAttributes')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        if m.get('Links') is not None:
            self.links = m.get('Links')
        if m.get('ParentSpanId') is not None:
            self.parent_span_id = m.get('ParentSpanId')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('SampleIds') is not None:
            self.sample_ids = m.get('SampleIds')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SpanId') is not None:
            self.span_id = m.get('SpanId')
        if m.get('SpanName') is not None:
            self.span_name = m.get('SpanName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class QueryTracesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        trace_lists: List[QueryTracesResponseBodyTraceLists] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.trace_lists = trace_lists

    def validate(self):
        if self.trace_lists:
            for k in self.trace_lists:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TraceLists'] = []
        if self.trace_lists is not None:
            for k in self.trace_lists:
                result['TraceLists'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.trace_lists = []
        if m.get('TraceLists') is not None:
            for k in m.get('TraceLists'):
                temp_model = QueryTracesResponseBodyTraceLists()
                self.trace_lists.append(temp_model.from_map(k))
        return self


class QueryTracesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTracesResponseBody = None,
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
            temp_model = QueryTracesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveAliClusterIdsFromPrometheusGlobalViewRequest(TeaModel):
    def __init__(
        self,
        cluster_ids: str = None,
        global_view_cluster_id: str = None,
        group_name: str = None,
        region_id: str = None,
    ):
        self.cluster_ids = cluster_ids
        self.global_view_cluster_id = global_view_cluster_id
        self.group_name = group_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_ids is not None:
            result['ClusterIds'] = self.cluster_ids
        if self.global_view_cluster_id is not None:
            result['GlobalViewClusterId'] = self.global_view_cluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterIds') is not None:
            self.cluster_ids = m.get('ClusterIds')
        if m.get('GlobalViewClusterId') is not None:
            self.global_view_cluster_id = m.get('GlobalViewClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RemoveAliClusterIdsFromPrometheusGlobalViewResponseBodyData(TeaModel):
    def __init__(
        self,
        info: str = None,
        msg: str = None,
        success: bool = None,
    ):
        self.info = info
        self.msg = msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info is not None:
            result['Info'] = self.info
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Info') is not None:
            self.info = m.get('Info')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveAliClusterIdsFromPrometheusGlobalViewResponseBody(TeaModel):
    def __init__(
        self,
        data: RemoveAliClusterIdsFromPrometheusGlobalViewResponseBodyData = None,
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
            temp_model = RemoveAliClusterIdsFromPrometheusGlobalViewResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveAliClusterIdsFromPrometheusGlobalViewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveAliClusterIdsFromPrometheusGlobalViewResponseBody = None,
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
            temp_model = RemoveAliClusterIdsFromPrometheusGlobalViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveSourcesFromPrometheusGlobalViewRequest(TeaModel):
    def __init__(
        self,
        global_view_cluster_id: str = None,
        group_name: str = None,
        region_id: str = None,
        source_names: str = None,
    ):
        self.global_view_cluster_id = global_view_cluster_id
        self.group_name = group_name
        self.region_id = region_id
        self.source_names = source_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.global_view_cluster_id is not None:
            result['GlobalViewClusterId'] = self.global_view_cluster_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_names is not None:
            result['SourceNames'] = self.source_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GlobalViewClusterId') is not None:
            self.global_view_cluster_id = m.get('GlobalViewClusterId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceNames') is not None:
            self.source_names = m.get('SourceNames')
        return self


class RemoveSourcesFromPrometheusGlobalViewResponseBodyData(TeaModel):
    def __init__(
        self,
        info: str = None,
        msg: str = None,
        success: bool = None,
    ):
        self.info = info
        self.msg = msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info is not None:
            result['Info'] = self.info
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Info') is not None:
            self.info = m.get('Info')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveSourcesFromPrometheusGlobalViewResponseBody(TeaModel):
    def __init__(
        self,
        data: RemoveSourcesFromPrometheusGlobalViewResponseBodyData = None,
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
            temp_model = RemoveSourcesFromPrometheusGlobalViewResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveSourcesFromPrometheusGlobalViewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveSourcesFromPrometheusGlobalViewResponseBody = None,
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
            temp_model = RemoveSourcesFromPrometheusGlobalViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveTraceAppConfigRequestSettings(TeaModel):
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


class SaveTraceAppConfigRequest(TeaModel):
    def __init__(
        self,
        pid: str = None,
        settings: List[SaveTraceAppConfigRequestSettings] = None,
    ):
        self.pid = pid
        self.settings = settings

    def validate(self):
        if self.settings:
            for k in self.settings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pid is not None:
            result['Pid'] = self.pid
        result['Settings'] = []
        if self.settings is not None:
            for k in self.settings:
                result['Settings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        self.settings = []
        if m.get('Settings') is not None:
            for k in m.get('Settings'):
                temp_model = SaveTraceAppConfigRequestSettings()
                self.settings.append(temp_model.from_map(k))
        return self


class SaveTraceAppConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
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


class SaveTraceAppConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveTraceAppConfigResponseBody = None,
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
            temp_model = SaveTraceAppConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchAlertContactRequest(TeaModel):
    def __init__(
        self,
        contact_ids: str = None,
        contact_name: str = None,
        current_page: str = None,
        email: str = None,
        page_size: str = None,
        phone: str = None,
        region_id: str = None,
    ):
        self.contact_ids = contact_ids
        self.contact_name = contact_name
        self.current_page = current_page
        self.email = email
        self.page_size = page_size
        self.phone = phone
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.email is not None:
            result['Email'] = self.email
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SearchAlertContactResponseBodyPageBeanContacts(TeaModel):
    def __init__(
        self,
        contact_id: int = None,
        contact_name: str = None,
        content: str = None,
        create_time: int = None,
        ding_robot: str = None,
        email: str = None,
        phone: str = None,
        system_noc: bool = None,
        update_time: int = None,
        user_id: str = None,
        webhook: str = None,
    ):
        self.contact_id = contact_id
        self.contact_name = contact_name
        self.content = content
        self.create_time = create_time
        self.ding_robot = ding_robot
        self.email = email
        self.phone = phone
        self.system_noc = system_noc
        self.update_time = update_time
        self.user_id = user_id
        self.webhook = webhook

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.ding_robot is not None:
            result['DingRobot'] = self.ding_robot
        if self.email is not None:
            result['Email'] = self.email
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.system_noc is not None:
            result['SystemNoc'] = self.system_noc
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.webhook is not None:
            result['Webhook'] = self.webhook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DingRobot') is not None:
            self.ding_robot = m.get('DingRobot')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('SystemNoc') is not None:
            self.system_noc = m.get('SystemNoc')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')
        return self


class SearchAlertContactResponseBodyPageBean(TeaModel):
    def __init__(
        self,
        contacts: List[SearchAlertContactResponseBodyPageBeanContacts] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.contacts = contacts
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.contacts:
            for k in self.contacts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Contacts'] = []
        if self.contacts is not None:
            for k in self.contacts:
                result['Contacts'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contacts = []
        if m.get('Contacts') is not None:
            for k in m.get('Contacts'):
                temp_model = SearchAlertContactResponseBodyPageBeanContacts()
                self.contacts.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchAlertContactResponseBody(TeaModel):
    def __init__(
        self,
        page_bean: SearchAlertContactResponseBodyPageBean = None,
        request_id: str = None,
    ):
        self.page_bean = page_bean
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = SearchAlertContactResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchAlertContactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchAlertContactResponseBody = None,
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
            temp_model = SearchAlertContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchAlertContactGroupRequest(TeaModel):
    def __init__(
        self,
        contact_group_ids: str = None,
        contact_group_name: str = None,
        contact_id: int = None,
        contact_name: str = None,
        is_detail: bool = None,
        region_id: str = None,
    ):
        self.contact_group_ids = contact_group_ids
        self.contact_group_name = contact_group_name
        self.contact_id = contact_id
        self.contact_name = contact_name
        self.is_detail = is_detail
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_ids is not None:
            result['ContactGroupIds'] = self.contact_group_ids
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.is_detail is not None:
            result['IsDetail'] = self.is_detail
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids = m.get('ContactGroupIds')
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('IsDetail') is not None:
            self.is_detail = m.get('IsDetail')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SearchAlertContactGroupResponseBodyContactGroupsContacts(TeaModel):
    def __init__(
        self,
        contact_id: int = None,
        contact_name: str = None,
        create_time: int = None,
        ding_robot: str = None,
        email: str = None,
        phone: str = None,
        system_noc: bool = None,
        update_time: int = None,
        user_id: str = None,
    ):
        self.contact_id = contact_id
        self.contact_name = contact_name
        self.create_time = create_time
        self.ding_robot = ding_robot
        self.email = email
        self.phone = phone
        self.system_noc = system_noc
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.ding_robot is not None:
            result['DingRobot'] = self.ding_robot
        if self.email is not None:
            result['Email'] = self.email
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.system_noc is not None:
            result['SystemNoc'] = self.system_noc
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DingRobot') is not None:
            self.ding_robot = m.get('DingRobot')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('SystemNoc') is not None:
            self.system_noc = m.get('SystemNoc')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SearchAlertContactGroupResponseBodyContactGroups(TeaModel):
    def __init__(
        self,
        contact_group_id: int = None,
        contact_group_name: str = None,
        contacts: List[SearchAlertContactGroupResponseBodyContactGroupsContacts] = None,
        create_time: int = None,
        update_time: int = None,
        user_id: str = None,
    ):
        self.contact_group_id = contact_group_id
        self.contact_group_name = contact_group_name
        self.contacts = contacts
        self.create_time = create_time
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        if self.contacts:
            for k in self.contacts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        result['Contacts'] = []
        if self.contacts is not None:
            for k in self.contacts:
                result['Contacts'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        self.contacts = []
        if m.get('Contacts') is not None:
            for k in m.get('Contacts'):
                temp_model = SearchAlertContactGroupResponseBodyContactGroupsContacts()
                self.contacts.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SearchAlertContactGroupResponseBody(TeaModel):
    def __init__(
        self,
        contact_groups: List[SearchAlertContactGroupResponseBodyContactGroups] = None,
        request_id: str = None,
    ):
        self.contact_groups = contact_groups
        self.request_id = request_id

    def validate(self):
        if self.contact_groups:
            for k in self.contact_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContactGroups'] = []
        if self.contact_groups is not None:
            for k in self.contact_groups:
                result['ContactGroups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact_groups = []
        if m.get('ContactGroups') is not None:
            for k in m.get('ContactGroups'):
                temp_model = SearchAlertContactGroupResponseBodyContactGroups()
                self.contact_groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchAlertContactGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchAlertContactGroupResponseBody = None,
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
            temp_model = SearchAlertContactGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchAlertHistoriesRequest(TeaModel):
    def __init__(
        self,
        alert_id: int = None,
        alert_type: int = None,
        current_page: int = None,
        end_time: int = None,
        page_size: int = None,
        region_id: str = None,
        start_time: int = None,
    ):
        self.alert_id = alert_id
        self.alert_type = alert_type
        self.current_page = current_page
        self.end_time = end_time
        self.page_size = page_size
        self.region_id = region_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class SearchAlertHistoriesResponseBodyPageBeanAlarmHistories(TeaModel):
    def __init__(
        self,
        alarm_content: str = None,
        alarm_response_code: int = None,
        alarm_sources: str = None,
        alarm_time: int = None,
        alarm_type: int = None,
        emails: str = None,
        id: int = None,
        phones: str = None,
        strategy_id: str = None,
        target: str = None,
        user_id: str = None,
    ):
        self.alarm_content = alarm_content
        self.alarm_response_code = alarm_response_code
        self.alarm_sources = alarm_sources
        self.alarm_time = alarm_time
        self.alarm_type = alarm_type
        self.emails = emails
        self.id = id
        self.phones = phones
        self.strategy_id = strategy_id
        self.target = target
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_content is not None:
            result['AlarmContent'] = self.alarm_content
        if self.alarm_response_code is not None:
            result['AlarmResponseCode'] = self.alarm_response_code
        if self.alarm_sources is not None:
            result['AlarmSources'] = self.alarm_sources
        if self.alarm_time is not None:
            result['AlarmTime'] = self.alarm_time
        if self.alarm_type is not None:
            result['AlarmType'] = self.alarm_type
        if self.emails is not None:
            result['Emails'] = self.emails
        if self.id is not None:
            result['Id'] = self.id
        if self.phones is not None:
            result['Phones'] = self.phones
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        if self.target is not None:
            result['Target'] = self.target
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmContent') is not None:
            self.alarm_content = m.get('AlarmContent')
        if m.get('AlarmResponseCode') is not None:
            self.alarm_response_code = m.get('AlarmResponseCode')
        if m.get('AlarmSources') is not None:
            self.alarm_sources = m.get('AlarmSources')
        if m.get('AlarmTime') is not None:
            self.alarm_time = m.get('AlarmTime')
        if m.get('AlarmType') is not None:
            self.alarm_type = m.get('AlarmType')
        if m.get('Emails') is not None:
            self.emails = m.get('Emails')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Phones') is not None:
            self.phones = m.get('Phones')
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SearchAlertHistoriesResponseBodyPageBean(TeaModel):
    def __init__(
        self,
        alarm_histories: List[SearchAlertHistoriesResponseBodyPageBeanAlarmHistories] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.alarm_histories = alarm_histories
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.alarm_histories:
            for k in self.alarm_histories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlarmHistories'] = []
        if self.alarm_histories is not None:
            for k in self.alarm_histories:
                result['AlarmHistories'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarm_histories = []
        if m.get('AlarmHistories') is not None:
            for k in m.get('AlarmHistories'):
                temp_model = SearchAlertHistoriesResponseBodyPageBeanAlarmHistories()
                self.alarm_histories.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchAlertHistoriesResponseBody(TeaModel):
    def __init__(
        self,
        page_bean: SearchAlertHistoriesResponseBodyPageBean = None,
        request_id: str = None,
    ):
        self.page_bean = page_bean
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = SearchAlertHistoriesResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchAlertHistoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchAlertHistoriesResponseBody = None,
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
            temp_model = SearchAlertHistoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchAlertHistorysRequest(TeaModel):
    def __init__(
        self,
        alert_id: int = None,
        alert_type: int = None,
        current_page: int = None,
        end_time: int = None,
        page_size: int = None,
        proxy_user_id: str = None,
        region_id: str = None,
        start_time: int = None,
    ):
        self.alert_id = alert_id
        self.alert_type = alert_type
        self.current_page = current_page
        self.end_time = end_time
        self.page_size = page_size
        self.proxy_user_id = proxy_user_id
        self.region_id = region_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class SearchAlertHistorysResponseBodyPageBeanAlertHistory(TeaModel):
    def __init__(
        self,
        alarm_content: str = None,
        alarm_response_code: str = None,
        alarm_time: int = None,
        alarm_type: int = None,
        alert_id: int = None,
        id: int = None,
        phones: str = None,
        tenant: str = None,
    ):
        self.alarm_content = alarm_content
        self.alarm_response_code = alarm_response_code
        self.alarm_time = alarm_time
        self.alarm_type = alarm_type
        self.alert_id = alert_id
        self.id = id
        self.phones = phones
        self.tenant = tenant

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_content is not None:
            result['AlarmContent'] = self.alarm_content
        if self.alarm_response_code is not None:
            result['AlarmResponseCode'] = self.alarm_response_code
        if self.alarm_time is not None:
            result['AlarmTime'] = self.alarm_time
        if self.alarm_type is not None:
            result['AlarmType'] = self.alarm_type
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.id is not None:
            result['Id'] = self.id
        if self.phones is not None:
            result['Phones'] = self.phones
        if self.tenant is not None:
            result['Tenant'] = self.tenant
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmContent') is not None:
            self.alarm_content = m.get('AlarmContent')
        if m.get('AlarmResponseCode') is not None:
            self.alarm_response_code = m.get('AlarmResponseCode')
        if m.get('AlarmTime') is not None:
            self.alarm_time = m.get('AlarmTime')
        if m.get('AlarmType') is not None:
            self.alarm_type = m.get('AlarmType')
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Phones') is not None:
            self.phones = m.get('Phones')
        if m.get('Tenant') is not None:
            self.tenant = m.get('Tenant')
        return self


class SearchAlertHistorysResponseBodyPageBean(TeaModel):
    def __init__(
        self,
        alert_history: List[SearchAlertHistorysResponseBodyPageBeanAlertHistory] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.alert_history = alert_history
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.alert_history:
            for k in self.alert_history:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlertHistory'] = []
        if self.alert_history is not None:
            for k in self.alert_history:
                result['AlertHistory'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_history = []
        if m.get('AlertHistory') is not None:
            for k in m.get('AlertHistory'):
                temp_model = SearchAlertHistorysResponseBodyPageBeanAlertHistory()
                self.alert_history.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchAlertHistorysResponseBody(TeaModel):
    def __init__(
        self,
        page_bean: SearchAlertHistorysResponseBodyPageBean = None,
        request_id: str = None,
    ):
        self.page_bean = page_bean
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = SearchAlertHistorysResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchAlertHistorysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchAlertHistorysResponseBody = None,
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
            temp_model = SearchAlertHistorysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchAlertRulesRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        current_page: int = None,
        page_size: int = None,
        pid: str = None,
        region_id: str = None,
        system_region_id: str = None,
        title: str = None,
        type: str = None,
    ):
        self.app_type = app_type
        self.current_page = current_page
        self.page_size = page_size
        self.pid = pid
        self.region_id = region_id
        self.system_region_id = system_region_id
        self.title = title
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.system_region_id is not None:
            result['SystemRegionId'] = self.system_region_id
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SystemRegionId') is not None:
            self.system_region_id = m.get('SystemRegionId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SearchAlertRulesResponseBodyPageBeanAlertRulesAlarmContext(TeaModel):
    def __init__(
        self,
        alarm_content_sub_title: str = None,
        alarm_content_template: str = None,
        content: str = None,
        sub_title: str = None,
    ):
        self.alarm_content_sub_title = alarm_content_sub_title
        self.alarm_content_template = alarm_content_template
        self.content = content
        self.sub_title = sub_title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_content_sub_title is not None:
            result['AlarmContentSubTitle'] = self.alarm_content_sub_title
        if self.alarm_content_template is not None:
            result['AlarmContentTemplate'] = self.alarm_content_template
        if self.content is not None:
            result['Content'] = self.content
        if self.sub_title is not None:
            result['SubTitle'] = self.sub_title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmContentSubTitle') is not None:
            self.alarm_content_sub_title = m.get('AlarmContentSubTitle')
        if m.get('AlarmContentTemplate') is not None:
            self.alarm_content_template = m.get('AlarmContentTemplate')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('SubTitle') is not None:
            self.sub_title = m.get('SubTitle')
        return self


class SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRuleRules(TeaModel):
    def __init__(
        self,
        aggregates: str = None,
        alias: str = None,
        measure: str = None,
        nvalue: int = None,
        operator: str = None,
        value: float = None,
    ):
        self.aggregates = aggregates
        self.alias = alias
        self.measure = measure
        self.nvalue = nvalue
        self.operator = operator
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregates is not None:
            result['Aggregates'] = self.aggregates
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.measure is not None:
            result['Measure'] = self.measure
        if self.nvalue is not None:
            result['NValue'] = self.nvalue
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aggregates') is not None:
            self.aggregates = m.get('Aggregates')
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Measure') is not None:
            self.measure = m.get('Measure')
        if m.get('NValue') is not None:
            self.nvalue = m.get('NValue')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRule(TeaModel):
    def __init__(
        self,
        operator: str = None,
        rules: List[SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRuleRules] = None,
    ):
        self.operator = operator
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
        if self.operator is not None:
            result['Operator'] = self.operator
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRuleRules()
                self.rules.append(temp_model.from_map(k))
        return self


class SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParamDimensions(TeaModel):
    def __init__(
        self,
        key: str = None,
        type: str = None,
        value: str = None,
    ):
        self.key = key
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
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParam(TeaModel):
    def __init__(
        self,
        app_group_id: str = None,
        app_id: str = None,
        dimensions: List[SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParamDimensions] = None,
        pid: str = None,
        type: str = None,
    ):
        self.app_group_id = app_group_id
        self.app_id = app_id
        self.dimensions = dimensions
        self.pid = pid
        self.type = type

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_group_id is not None:
            result['AppGroupId'] = self.app_group_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppGroupId') is not None:
            self.app_group_id = m.get('AppGroupId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParamDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SearchAlertRulesResponseBodyPageBeanAlertRulesNotice(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        notice_end_time: int = None,
        notice_start_time: int = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.notice_end_time = notice_end_time
        self.notice_start_time = notice_start_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.notice_end_time is not None:
            result['NoticeEndTime'] = self.notice_end_time
        if self.notice_start_time is not None:
            result['NoticeStartTime'] = self.notice_start_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('NoticeEndTime') is not None:
            self.notice_end_time = m.get('NoticeEndTime')
        if m.get('NoticeStartTime') is not None:
            self.notice_start_time = m.get('NoticeStartTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class SearchAlertRulesResponseBodyPageBeanAlertRules(TeaModel):
    def __init__(
        self,
        alarm_context: SearchAlertRulesResponseBodyPageBeanAlertRulesAlarmContext = None,
        alert_level: str = None,
        alert_rule: SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRule = None,
        alert_title: str = None,
        alert_type: int = None,
        alert_version: int = None,
        alert_ways: List[str] = None,
        config: str = None,
        contact_group_id_list: str = None,
        contact_group_ids: str = None,
        create_time: int = None,
        host_by_alert_manager: bool = None,
        id: int = None,
        metric_param: SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParam = None,
        notice: SearchAlertRulesResponseBodyPageBeanAlertRulesNotice = None,
        region_id: str = None,
        status: str = None,
        task_id: int = None,
        task_status: str = None,
        title: str = None,
        update_time: int = None,
        user_id: str = None,
    ):
        self.alarm_context = alarm_context
        self.alert_level = alert_level
        self.alert_rule = alert_rule
        self.alert_title = alert_title
        self.alert_type = alert_type
        self.alert_version = alert_version
        self.alert_ways = alert_ways
        self.config = config
        self.contact_group_id_list = contact_group_id_list
        self.contact_group_ids = contact_group_ids
        self.create_time = create_time
        self.host_by_alert_manager = host_by_alert_manager
        self.id = id
        self.metric_param = metric_param
        self.notice = notice
        self.region_id = region_id
        self.status = status
        self.task_id = task_id
        self.task_status = task_status
        self.title = title
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        if self.alarm_context:
            self.alarm_context.validate()
        if self.alert_rule:
            self.alert_rule.validate()
        if self.metric_param:
            self.metric_param.validate()
        if self.notice:
            self.notice.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_context is not None:
            result['AlarmContext'] = self.alarm_context.to_map()
        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level
        if self.alert_rule is not None:
            result['AlertRule'] = self.alert_rule.to_map()
        if self.alert_title is not None:
            result['AlertTitle'] = self.alert_title
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_version is not None:
            result['AlertVersion'] = self.alert_version
        if self.alert_ways is not None:
            result['AlertWays'] = self.alert_ways
        if self.config is not None:
            result['Config'] = self.config
        if self.contact_group_id_list is not None:
            result['ContactGroupIdList'] = self.contact_group_id_list
        if self.contact_group_ids is not None:
            result['ContactGroupIds'] = self.contact_group_ids
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.host_by_alert_manager is not None:
            result['HostByAlertManager'] = self.host_by_alert_manager
        if self.id is not None:
            result['Id'] = self.id
        if self.metric_param is not None:
            result['MetricParam'] = self.metric_param.to_map()
        if self.notice is not None:
            result['Notice'] = self.notice.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.title is not None:
            result['Title'] = self.title
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmContext') is not None:
            temp_model = SearchAlertRulesResponseBodyPageBeanAlertRulesAlarmContext()
            self.alarm_context = temp_model.from_map(m['AlarmContext'])
        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')
        if m.get('AlertRule') is not None:
            temp_model = SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRule()
            self.alert_rule = temp_model.from_map(m['AlertRule'])
        if m.get('AlertTitle') is not None:
            self.alert_title = m.get('AlertTitle')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertVersion') is not None:
            self.alert_version = m.get('AlertVersion')
        if m.get('AlertWays') is not None:
            self.alert_ways = m.get('AlertWays')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ContactGroupIdList') is not None:
            self.contact_group_id_list = m.get('ContactGroupIdList')
        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids = m.get('ContactGroupIds')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('HostByAlertManager') is not None:
            self.host_by_alert_manager = m.get('HostByAlertManager')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MetricParam') is not None:
            temp_model = SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParam()
            self.metric_param = temp_model.from_map(m['MetricParam'])
        if m.get('Notice') is not None:
            temp_model = SearchAlertRulesResponseBodyPageBeanAlertRulesNotice()
            self.notice = temp_model.from_map(m['Notice'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SearchAlertRulesResponseBodyPageBean(TeaModel):
    def __init__(
        self,
        alert_rules: List[SearchAlertRulesResponseBodyPageBeanAlertRules] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.alert_rules = alert_rules
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.alert_rules:
            for k in self.alert_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlertRules'] = []
        if self.alert_rules is not None:
            for k in self.alert_rules:
                result['AlertRules'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_rules = []
        if m.get('AlertRules') is not None:
            for k in m.get('AlertRules'):
                temp_model = SearchAlertRulesResponseBodyPageBeanAlertRules()
                self.alert_rules.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchAlertRulesResponseBody(TeaModel):
    def __init__(
        self,
        page_bean: SearchAlertRulesResponseBodyPageBean = None,
        request_id: str = None,
    ):
        self.page_bean = page_bean
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = SearchAlertRulesResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchAlertRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchAlertRulesResponseBody = None,
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
            temp_model = SearchAlertRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchEventsRequest(TeaModel):
    def __init__(
        self,
        alert_id: int = None,
        alert_type: int = None,
        app_type: str = None,
        current_page: int = None,
        end_time: int = None,
        is_trigger: int = None,
        page_size: int = None,
        pid: str = None,
        region_id: str = None,
        start_time: int = None,
    ):
        self.alert_id = alert_id
        self.alert_type = alert_type
        self.app_type = app_type
        self.current_page = current_page
        self.end_time = end_time
        self.is_trigger = is_trigger
        self.page_size = page_size
        self.pid = pid
        self.region_id = region_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.is_trigger is not None:
            result['IsTrigger'] = self.is_trigger
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IsTrigger') is not None:
            self.is_trigger = m.get('IsTrigger')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class SearchEventsResponseBodyPageBeanEvent(TeaModel):
    def __init__(
        self,
        alert_id: int = None,
        alert_name: str = None,
        alert_rule: str = None,
        alert_type: int = None,
        event_level: str = None,
        event_time: int = None,
        id: int = None,
        links: List[str] = None,
        message: str = None,
    ):
        self.alert_id = alert_id
        self.alert_name = alert_name
        self.alert_rule = alert_rule
        self.alert_type = alert_type
        self.event_level = event_level
        self.event_time = event_time
        self.id = id
        self.links = links
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.alert_rule is not None:
            result['AlertRule'] = self.alert_rule
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.event_level is not None:
            result['EventLevel'] = self.event_level
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.id is not None:
            result['Id'] = self.id
        if self.links is not None:
            result['Links'] = self.links
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('AlertRule') is not None:
            self.alert_rule = m.get('AlertRule')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('EventLevel') is not None:
            self.event_level = m.get('EventLevel')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Links') is not None:
            self.links = m.get('Links')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SearchEventsResponseBodyPageBean(TeaModel):
    def __init__(
        self,
        event: List[SearchEventsResponseBodyPageBeanEvent] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.event = event
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.event:
            for k in self.event:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Event'] = []
        if self.event is not None:
            for k in self.event:
                result['Event'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event = []
        if m.get('Event') is not None:
            for k in m.get('Event'):
                temp_model = SearchEventsResponseBodyPageBeanEvent()
                self.event.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchEventsResponseBody(TeaModel):
    def __init__(
        self,
        is_trigger: int = None,
        page_bean: SearchEventsResponseBodyPageBean = None,
        request_id: str = None,
    ):
        self.is_trigger = is_trigger
        self.page_bean = page_bean
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_trigger is not None:
            result['IsTrigger'] = self.is_trigger
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsTrigger') is not None:
            self.is_trigger = m.get('IsTrigger')
        if m.get('PageBean') is not None:
            temp_model = SearchEventsResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchEventsResponseBody = None,
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
            temp_model = SearchEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchRetcodeAppByPageRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        retcode_app_name: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.retcode_app_name = retcode_app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.retcode_app_name is not None:
            result['RetcodeAppName'] = self.retcode_app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RetcodeAppName') is not None:
            self.retcode_app_name = m.get('RetcodeAppName')
        return self


class SearchRetcodeAppByPageResponseBodyPageBeanRetcodeApps(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        create_time: int = None,
        pid: str = None,
        region_id: str = None,
        retcode_app_type: str = None,
        type: str = None,
        update_time: int = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.create_time = create_time
        self.pid = pid
        self.region_id = region_id
        self.retcode_app_type = retcode_app_type
        self.type = type
        self.update_time = update_time
        self.user_id = user_id

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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.retcode_app_type is not None:
            result['RetcodeAppType'] = self.retcode_app_type
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RetcodeAppType') is not None:
            self.retcode_app_type = m.get('RetcodeAppType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SearchRetcodeAppByPageResponseBodyPageBean(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        retcode_apps: List[SearchRetcodeAppByPageResponseBodyPageBeanRetcodeApps] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.retcode_apps = retcode_apps
        self.total_count = total_count

    def validate(self):
        if self.retcode_apps:
            for k in self.retcode_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['RetcodeApps'] = []
        if self.retcode_apps is not None:
            for k in self.retcode_apps:
                result['RetcodeApps'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.retcode_apps = []
        if m.get('RetcodeApps') is not None:
            for k in m.get('RetcodeApps'):
                temp_model = SearchRetcodeAppByPageResponseBodyPageBeanRetcodeApps()
                self.retcode_apps.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchRetcodeAppByPageResponseBody(TeaModel):
    def __init__(
        self,
        page_bean: SearchRetcodeAppByPageResponseBodyPageBean = None,
        request_id: str = None,
    ):
        self.page_bean = page_bean
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = SearchRetcodeAppByPageResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchRetcodeAppByPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchRetcodeAppByPageResponseBody = None,
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
            temp_model = SearchRetcodeAppByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTagNamesRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        pid: str = None,
        region_id: str = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.pid = pid
        self.region_id = region_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class SearchTagNamesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tags: List[str] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class SearchTagNamesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchTagNamesResponseBody = None,
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
            temp_model = SearchTagNamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTagValuesRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        pid: str = None,
        region_id: str = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.pid = pid
        self.region_id = region_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class SearchTagValuesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        values: List[str] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class SearchTagValuesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchTagValuesResponseBody = None,
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
            temp_model = SearchTagValuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTraceAppByNameRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        trace_app_name: str = None,
    ):
        self.region_id = region_id
        self.trace_app_name = trace_app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.trace_app_name is not None:
            result['TraceAppName'] = self.trace_app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TraceAppName') is not None:
            self.trace_app_name = m.get('TraceAppName')
        return self


class SearchTraceAppByNameResponseBodyTraceApps(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        create_time: int = None,
        labels: List[str] = None,
        pid: str = None,
        region_id: str = None,
        show: bool = None,
        type: str = None,
        update_time: int = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.create_time = create_time
        self.labels = labels
        self.pid = pid
        self.region_id = region_id
        self.show = show
        self.type = type
        self.update_time = update_time
        self.user_id = user_id

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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.show is not None:
            result['Show'] = self.show
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Show') is not None:
            self.show = m.get('Show')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SearchTraceAppByNameResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        trace_apps: List[SearchTraceAppByNameResponseBodyTraceApps] = None,
    ):
        self.request_id = request_id
        self.trace_apps = trace_apps

    def validate(self):
        if self.trace_apps:
            for k in self.trace_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TraceApps'] = []
        if self.trace_apps is not None:
            for k in self.trace_apps:
                result['TraceApps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.trace_apps = []
        if m.get('TraceApps') is not None:
            for k in m.get('TraceApps'):
                temp_model = SearchTraceAppByNameResponseBodyTraceApps()
                self.trace_apps.append(temp_model.from_map(k))
        return self


class SearchTraceAppByNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchTraceAppByNameResponseBody = None,
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
            temp_model = SearchTraceAppByNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTraceAppByPageRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        trace_app_name: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.trace_app_name = trace_app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.trace_app_name is not None:
            result['TraceAppName'] = self.trace_app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TraceAppName') is not None:
            self.trace_app_name = m.get('TraceAppName')
        return self


class SearchTraceAppByPageResponseBodyPageBeanTraceApps(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        create_time: int = None,
        labels: List[str] = None,
        pid: str = None,
        region_id: str = None,
        show: bool = None,
        type: str = None,
        update_time: int = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.create_time = create_time
        self.labels = labels
        self.pid = pid
        self.region_id = region_id
        self.show = show
        self.type = type
        self.update_time = update_time
        self.user_id = user_id

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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.show is not None:
            result['Show'] = self.show
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Show') is not None:
            self.show = m.get('Show')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SearchTraceAppByPageResponseBodyPageBean(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        trace_apps: List[SearchTraceAppByPageResponseBodyPageBeanTraceApps] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.trace_apps = trace_apps

    def validate(self):
        if self.trace_apps:
            for k in self.trace_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['TraceApps'] = []
        if self.trace_apps is not None:
            for k in self.trace_apps:
                result['TraceApps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.trace_apps = []
        if m.get('TraceApps') is not None:
            for k in m.get('TraceApps'):
                temp_model = SearchTraceAppByPageResponseBodyPageBeanTraceApps()
                self.trace_apps.append(temp_model.from_map(k))
        return self


class SearchTraceAppByPageResponseBody(TeaModel):
    def __init__(
        self,
        page_bean: SearchTraceAppByPageResponseBodyPageBean = None,
        request_id: str = None,
    ):
        self.page_bean = page_bean
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = SearchTraceAppByPageResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchTraceAppByPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchTraceAppByPageResponseBody = None,
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
            temp_model = SearchTraceAppByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTracesRequestExclusionFilters(TeaModel):
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


class SearchTracesRequestTag(TeaModel):
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


class SearchTracesRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        exclusion_filters: List[SearchTracesRequestExclusionFilters] = None,
        min_duration: int = None,
        operation_name: str = None,
        pid: str = None,
        region_id: str = None,
        reverse: bool = None,
        service_ip: str = None,
        service_name: str = None,
        start_time: int = None,
        tag: List[SearchTracesRequestTag] = None,
    ):
        self.end_time = end_time
        self.exclusion_filters = exclusion_filters
        self.min_duration = min_duration
        self.operation_name = operation_name
        self.pid = pid
        self.region_id = region_id
        self.reverse = reverse
        self.service_ip = service_ip
        self.service_name = service_name
        self.start_time = start_time
        self.tag = tag

    def validate(self):
        if self.exclusion_filters:
            for k in self.exclusion_filters:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['ExclusionFilters'] = []
        if self.exclusion_filters is not None:
            for k in self.exclusion_filters:
                result['ExclusionFilters'].append(k.to_map() if k else None)
        if self.min_duration is not None:
            result['MinDuration'] = self.min_duration
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.exclusion_filters = []
        if m.get('ExclusionFilters') is not None:
            for k in m.get('ExclusionFilters'):
                temp_model = SearchTracesRequestExclusionFilters()
                self.exclusion_filters.append(temp_model.from_map(k))
        if m.get('MinDuration') is not None:
            self.min_duration = m.get('MinDuration')
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = SearchTracesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class SearchTracesResponseBodyTraceInfos(TeaModel):
    def __init__(
        self,
        duration: int = None,
        operation_name: str = None,
        service_ip: str = None,
        service_name: str = None,
        timestamp: int = None,
        trace_id: str = None,
    ):
        self.duration = duration
        self.operation_name = operation_name
        self.service_ip = service_ip
        self.service_name = service_name
        self.timestamp = timestamp
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class SearchTracesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        trace_infos: List[SearchTracesResponseBodyTraceInfos] = None,
    ):
        self.request_id = request_id
        self.trace_infos = trace_infos

    def validate(self):
        if self.trace_infos:
            for k in self.trace_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TraceInfos'] = []
        if self.trace_infos is not None:
            for k in self.trace_infos:
                result['TraceInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.trace_infos = []
        if m.get('TraceInfos') is not None:
            for k in m.get('TraceInfos'):
                temp_model = SearchTracesResponseBodyTraceInfos()
                self.trace_infos.append(temp_model.from_map(k))
        return self


class SearchTracesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchTracesResponseBody = None,
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
            temp_model = SearchTracesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTracesByPageRequestExclusionFilters(TeaModel):
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


class SearchTracesByPageRequestTags(TeaModel):
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


class SearchTracesByPageRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        exclusion_filters: List[SearchTracesByPageRequestExclusionFilters] = None,
        min_duration: int = None,
        operation_name: str = None,
        page_number: int = None,
        page_size: int = None,
        pid: str = None,
        region_id: str = None,
        reverse: bool = None,
        service_ip: str = None,
        service_name: str = None,
        start_time: int = None,
        tags: List[SearchTracesByPageRequestTags] = None,
    ):
        self.end_time = end_time
        self.exclusion_filters = exclusion_filters
        self.min_duration = min_duration
        self.operation_name = operation_name
        self.page_number = page_number
        self.page_size = page_size
        self.pid = pid
        self.region_id = region_id
        self.reverse = reverse
        self.service_ip = service_ip
        self.service_name = service_name
        self.start_time = start_time
        self.tags = tags

    def validate(self):
        if self.exclusion_filters:
            for k in self.exclusion_filters:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['ExclusionFilters'] = []
        if self.exclusion_filters is not None:
            for k in self.exclusion_filters:
                result['ExclusionFilters'].append(k.to_map() if k else None)
        if self.min_duration is not None:
            result['MinDuration'] = self.min_duration
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.exclusion_filters = []
        if m.get('ExclusionFilters') is not None:
            for k in m.get('ExclusionFilters'):
                temp_model = SearchTracesByPageRequestExclusionFilters()
                self.exclusion_filters.append(temp_model.from_map(k))
        if m.get('MinDuration') is not None:
            self.min_duration = m.get('MinDuration')
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = SearchTracesByPageRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class SearchTracesByPageResponseBodyPageBeanTraceInfos(TeaModel):
    def __init__(
        self,
        duration: int = None,
        operation_name: str = None,
        service_ip: str = None,
        service_name: str = None,
        timestamp: int = None,
        trace_id: str = None,
    ):
        self.duration = duration
        self.operation_name = operation_name
        self.service_ip = service_ip
        self.service_name = service_name
        self.timestamp = timestamp
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class SearchTracesByPageResponseBodyPageBean(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
        trace_infos: List[SearchTracesByPageResponseBodyPageBeanTraceInfos] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total = total
        self.trace_infos = trace_infos

    def validate(self):
        if self.trace_infos:
            for k in self.trace_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        result['TraceInfos'] = []
        if self.trace_infos is not None:
            for k in self.trace_infos:
                result['TraceInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.trace_infos = []
        if m.get('TraceInfos') is not None:
            for k in m.get('TraceInfos'):
                temp_model = SearchTracesByPageResponseBodyPageBeanTraceInfos()
                self.trace_infos.append(temp_model.from_map(k))
        return self


class SearchTracesByPageResponseBody(TeaModel):
    def __init__(
        self,
        page_bean: SearchTracesByPageResponseBodyPageBean = None,
        request_id: str = None,
    ):
        self.page_bean = page_bean
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = SearchTracesByPageResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchTracesByPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchTracesByPageResponseBody = None,
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
            temp_model = SearchTracesByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendTTSVerifyLinkRequest(TeaModel):
    def __init__(
        self,
        contact_id: int = None,
        phone: str = None,
    ):
        # 告警联系人ID
        self.contact_id = contact_id
        # 告警联系人手机号码
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class SendTTSVerifyLinkResponseBody(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.is_success = is_success
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendTTSVerifyLinkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendTTSVerifyLinkResponseBody = None,
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
            temp_model = SendTTSVerifyLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetRetcodeShareStatusRequest(TeaModel):
    def __init__(
        self,
        pid: str = None,
        status: bool = None,
    ):
        self.pid = pid
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SetRetcodeShareStatusResponseBody(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetRetcodeShareStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetRetcodeShareStatusResponseBody = None,
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
            temp_model = SetRetcodeShareStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartAlertRequest(TeaModel):
    def __init__(
        self,
        alert_id: str = None,
        region_id: str = None,
    ):
        self.alert_id = alert_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StartAlertResponseBody(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartAlertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartAlertResponseBody = None,
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
            temp_model = StartAlertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopAlertRequest(TeaModel):
    def __init__(
        self,
        alert_id: str = None,
        region_id: str = None,
    ):
        self.alert_id = alert_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StopAlertResponseBody(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopAlertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopAlertResponseBody = None,
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
            temp_model = StopAlertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
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
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TurnOnSecondSwitchRequest(TeaModel):
    def __init__(
        self,
        pid: str = None,
        proxy_user_id: str = None,
        release_start_time: int = None,
    ):
        self.pid = pid
        self.proxy_user_id = proxy_user_id
        self.release_start_time = release_start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.release_start_time is not None:
            result['ReleaseStartTime'] = self.release_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('ReleaseStartTime') is not None:
            self.release_start_time = m.get('ReleaseStartTime')
        return self


class TurnOnSecondSwitchResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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


class TurnOnSecondSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TurnOnSecondSwitchResponseBody = None,
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
            temp_model = TurnOnSecondSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UninstallManagedPrometheusRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_type: str = None,
        region_id: str = None,
        vpc_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_type = cluster_type
        self.region_id = region_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class UninstallManagedPrometheusResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UninstallManagedPrometheusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UninstallManagedPrometheusResponseBody = None,
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
            temp_model = UninstallManagedPrometheusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UninstallPromClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UninstallPromClusterResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
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


class UninstallPromClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UninstallPromClusterResponseBody = None,
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
            temp_model = UninstallPromClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        self.all = all
        self.resource_id = resource_id
        self.resource_type = resource_type
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


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAlertContactRequest(TeaModel):
    def __init__(
        self,
        contact_id: int = None,
        contact_name: str = None,
        ding_robot_webhook_url: str = None,
        email: str = None,
        phone_num: str = None,
        region_id: str = None,
        system_noc: bool = None,
    ):
        self.contact_id = contact_id
        self.contact_name = contact_name
        self.ding_robot_webhook_url = ding_robot_webhook_url
        self.email = email
        self.phone_num = phone_num
        self.region_id = region_id
        self.system_noc = system_noc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.ding_robot_webhook_url is not None:
            result['DingRobotWebhookUrl'] = self.ding_robot_webhook_url
        if self.email is not None:
            result['Email'] = self.email
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.system_noc is not None:
            result['SystemNoc'] = self.system_noc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('DingRobotWebhookUrl') is not None:
            self.ding_robot_webhook_url = m.get('DingRobotWebhookUrl')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SystemNoc') is not None:
            self.system_noc = m.get('SystemNoc')
        return self


class UpdateAlertContactResponseBody(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAlertContactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAlertContactResponseBody = None,
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
            temp_model = UpdateAlertContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAlertContactGroupRequest(TeaModel):
    def __init__(
        self,
        contact_group_id: int = None,
        contact_group_name: str = None,
        contact_ids: str = None,
        region_id: str = None,
    ):
        self.contact_group_id = contact_group_id
        self.contact_group_name = contact_group_name
        self.contact_ids = contact_ids
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateAlertContactGroupResponseBody(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAlertContactGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAlertContactGroupResponseBody = None,
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
            temp_model = UpdateAlertContactGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAlertRuleRequest(TeaModel):
    def __init__(
        self,
        alert_id: int = None,
        contact_group_ids: str = None,
        is_auto_start: bool = None,
        region_id: str = None,
        templage_alert_config: str = None,
    ):
        self.alert_id = alert_id
        self.contact_group_ids = contact_group_ids
        self.is_auto_start = is_auto_start
        self.region_id = region_id
        self.templage_alert_config = templage_alert_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.contact_group_ids is not None:
            result['ContactGroupIds'] = self.contact_group_ids
        if self.is_auto_start is not None:
            result['IsAutoStart'] = self.is_auto_start
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.templage_alert_config is not None:
            result['TemplageAlertConfig'] = self.templage_alert_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids = m.get('ContactGroupIds')
        if m.get('IsAutoStart') is not None:
            self.is_auto_start = m.get('IsAutoStart')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplageAlertConfig') is not None:
            self.templage_alert_config = m.get('TemplageAlertConfig')
        return self


class UpdateAlertRuleResponseBody(TeaModel):
    def __init__(
        self,
        alert_id: int = None,
        data: str = None,
        request_id: str = None,
    ):
        self.alert_id = alert_id
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAlertRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAlertRuleResponseBody = None,
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
            temp_model = UpdateAlertRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDispatchRuleRequest(TeaModel):
    def __init__(
        self,
        dispatch_rule: str = None,
        region_id: str = None,
    ):
        self.dispatch_rule = dispatch_rule
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dispatch_rule is not None:
            result['DispatchRule'] = self.dispatch_rule
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DispatchRule') is not None:
            self.dispatch_rule = m.get('DispatchRule')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateDispatchRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateDispatchRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDispatchRuleResponseBody = None,
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
            temp_model = UpdateDispatchRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePrometheusAlertRuleRequest(TeaModel):
    def __init__(
        self,
        alert_id: int = None,
        alert_name: str = None,
        annotations: str = None,
        cluster_id: str = None,
        dispatch_rule_id: int = None,
        duration: str = None,
        expression: str = None,
        labels: str = None,
        message: str = None,
        notify_type: str = None,
        region_id: str = None,
        type: str = None,
    ):
        self.alert_id = alert_id
        self.alert_name = alert_name
        self.annotations = annotations
        self.cluster_id = cluster_id
        self.dispatch_rule_id = dispatch_rule_id
        self.duration = duration
        self.expression = expression
        self.labels = labels
        self.message = message
        self.notify_type = notify_type
        self.region_id = region_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.annotations is not None:
            result['Annotations'] = self.annotations
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.message is not None:
            result['Message'] = self.message
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations(TeaModel):
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
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels(TeaModel):
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
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRule(TeaModel):
    def __init__(
        self,
        alert_id: int = None,
        alert_name: str = None,
        annotations: List[UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations] = None,
        cluster_id: str = None,
        dispatch_rule_id: int = None,
        duration: str = None,
        expression: str = None,
        labels: List[UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels] = None,
        message: str = None,
        notify_type: str = None,
        status: int = None,
        type: str = None,
    ):
        self.alert_id = alert_id
        self.alert_name = alert_name
        self.annotations = annotations
        self.cluster_id = cluster_id
        self.dispatch_rule_id = dispatch_rule_id
        self.duration = duration
        self.expression = expression
        self.labels = labels
        self.message = message
        self.notify_type = notify_type
        self.status = status
        self.type = type

    def validate(self):
        if self.annotations:
            for k in self.annotations:
                if k:
                    k.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        result['Annotations'] = []
        if self.annotations is not None:
            for k in self.annotations:
                result['Annotations'].append(k.to_map() if k else None)
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.dispatch_rule_id is not None:
            result['DispatchRuleId'] = self.dispatch_rule_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expression is not None:
            result['Expression'] = self.expression
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        self.annotations = []
        if m.get('Annotations') is not None:
            for k in m.get('Annotations'):
                temp_model = UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRuleAnnotations()
                self.annotations.append(temp_model.from_map(k))
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DispatchRuleId') is not None:
            self.dispatch_rule_id = m.get('DispatchRuleId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRuleLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdatePrometheusAlertRuleResponseBody(TeaModel):
    def __init__(
        self,
        prometheus_alert_rule: UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRule = None,
        request_id: str = None,
    ):
        self.prometheus_alert_rule = prometheus_alert_rule
        self.request_id = request_id

    def validate(self):
        if self.prometheus_alert_rule:
            self.prometheus_alert_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prometheus_alert_rule is not None:
            result['PrometheusAlertRule'] = self.prometheus_alert_rule.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrometheusAlertRule') is not None:
            temp_model = UpdatePrometheusAlertRuleResponseBodyPrometheusAlertRule()
            self.prometheus_alert_rule = temp_model.from_map(m['PrometheusAlertRule'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePrometheusAlertRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePrometheusAlertRuleResponseBody = None,
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
            temp_model = UpdatePrometheusAlertRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWebhookRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        contact_id: int = None,
        contact_name: str = None,
        http_headers: str = None,
        http_params: str = None,
        method: str = None,
        recover_body: str = None,
        region_id: str = None,
        url: str = None,
    ):
        self.body = body
        self.contact_id = contact_id
        self.contact_name = contact_name
        self.http_headers = http_headers
        self.http_params = http_params
        self.method = method
        self.recover_body = recover_body
        self.region_id = region_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.http_headers is not None:
            result['HttpHeaders'] = self.http_headers
        if self.http_params is not None:
            result['HttpParams'] = self.http_params
        if self.method is not None:
            result['Method'] = self.method
        if self.recover_body is not None:
            result['RecoverBody'] = self.recover_body
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('HttpHeaders') is not None:
            self.http_headers = m.get('HttpHeaders')
        if m.get('HttpParams') is not None:
            self.http_params = m.get('HttpParams')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('RecoverBody') is not None:
            self.recover_body = m.get('RecoverBody')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class UpdateWebhookResponseBody(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateWebhookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateWebhookResponseBody = None,
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
            temp_model = UpdateWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadRequest(TeaModel):
    def __init__(
        self,
        file: str = None,
        file_name: str = None,
        pid: str = None,
        region_id: str = None,
        version: str = None,
    ):
        self.file = file
        self.file_name = file_name
        self.pid = pid
        self.region_id = region_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file is not None:
            result['File'] = self.file
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('File') is not None:
            self.file = m.get('File')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class UploadResponseBody(TeaModel):
    def __init__(
        self,
        fid: str = None,
        file_name: str = None,
        request_id: str = None,
        upload_time: str = None,
        version: str = None,
    ):
        self.fid = fid
        self.file_name = file_name
        # Id of the request
        self.request_id = request_id
        self.upload_time = upload_time
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fid is not None:
            result['Fid'] = self.fid
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.upload_time is not None:
            result['UploadTime'] = self.upload_time
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fid') is not None:
            self.fid = m.get('Fid')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UploadTime') is not None:
            self.upload_time = m.get('UploadTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class UploadResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadResponseBody = None,
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
            temp_model = UploadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


