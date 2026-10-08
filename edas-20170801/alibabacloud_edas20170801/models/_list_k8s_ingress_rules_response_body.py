# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class ListK8sIngressRulesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.ListK8sIngressRulesResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The response data.
        self.data = data
        # The message that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListK8sIngressRulesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListK8sIngressRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        ingress_confs: List[main_models.ListK8sIngressRulesResponseBodyDataIngressConfs] = None,
        region_id: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The cluster name.
        self.cluster_name = cluster_name
        # The Ingresses.
        self.ingress_confs = ingress_confs
        # The ID of the Alibaba Cloud region.
        self.region_id = region_id

    def validate(self):
        if self.ingress_confs:
            for v1 in self.ingress_confs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        result['IngressConfs'] = []
        if self.ingress_confs is not None:
            for k1 in self.ingress_confs:
                result['IngressConfs'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        self.ingress_confs = []
        if m.get('IngressConfs') is not None:
            for k1 in m.get('IngressConfs'):
                temp_model = main_models.ListK8sIngressRulesResponseBodyDataIngressConfs()
                self.ingress_confs.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class ListK8sIngressRulesResponseBodyDataIngressConfs(DaraModel):
    def __init__(
        self,
        alb_id: str = None,
        annotations: str = None,
        creation_time: str = None,
        dashboard_url: str = None,
        endpoint: str = None,
        ingress_type: str = None,
        labels: str = None,
        mse_gateway_id: str = None,
        mse_gateway_name: str = None,
        name: str = None,
        namespace: str = None,
        offical_basic_url: str = None,
        offical_request_url: str = None,
        rules: List[main_models.ListK8sIngressRulesResponseBodyDataIngressConfsRules] = None,
        ssl_redirect: bool = None,
    ):
        # The ID of the ALB instance.
        self.alb_id = alb_id
        # The annotations.
        self.annotations = annotations
        # The time when the Ingress was created.
        self.creation_time = creation_time
        # The monitoring URL of the Ingress.
        self.dashboard_url = dashboard_url
        # The IP address of the Ingress.
        self.endpoint = endpoint
        # The Ingress type. Valid values:
        # 
        # *   **NginxIngress**: NGINX Ingress controller
        # *   **AlbIngress**: ALB Ingress controller
        # 
        # Default value: NginxIngress.
        self.ingress_type = ingress_type
        # The tags.
        self.labels = labels
        # The ID of the MSE gateway.
        self.mse_gateway_id = mse_gateway_id
        # The name of the MSE gateway.
        self.mse_gateway_name = mse_gateway_name
        # The Ingress name.
        self.name = name
        # The Kubernetes namespace to which the Ingress belongs.
        self.namespace = namespace
        # The URL used for basic monitoring of the open source version.
        self.offical_basic_url = offical_basic_url
        # The URL used for request performance monitoring of the open source version.
        self.offical_request_url = offical_request_url
        # The routing rules.
        self.rules = rules
        # Indicates whether SSL redirection is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.ssl_redirect = ssl_redirect

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alb_id is not None:
            result['AlbId'] = self.alb_id

        if self.annotations is not None:
            result['Annotations'] = self.annotations

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.dashboard_url is not None:
            result['DashboardUrl'] = self.dashboard_url

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.ingress_type is not None:
            result['IngressType'] = self.ingress_type

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.mse_gateway_id is not None:
            result['MseGatewayId'] = self.mse_gateway_id

        if self.mse_gateway_name is not None:
            result['MseGatewayName'] = self.mse_gateway_name

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.offical_basic_url is not None:
            result['OfficalBasicUrl'] = self.offical_basic_url

        if self.offical_request_url is not None:
            result['OfficalRequestUrl'] = self.offical_request_url

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.ssl_redirect is not None:
            result['SslRedirect'] = self.ssl_redirect

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbId') is not None:
            self.alb_id = m.get('AlbId')

        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DashboardUrl') is not None:
            self.dashboard_url = m.get('DashboardUrl')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('IngressType') is not None:
            self.ingress_type = m.get('IngressType')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('MseGatewayId') is not None:
            self.mse_gateway_id = m.get('MseGatewayId')

        if m.get('MseGatewayName') is not None:
            self.mse_gateway_name = m.get('MseGatewayName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('OfficalBasicUrl') is not None:
            self.offical_basic_url = m.get('OfficalBasicUrl')

        if m.get('OfficalRequestUrl') is not None:
            self.offical_request_url = m.get('OfficalRequestUrl')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.ListK8sIngressRulesResponseBodyDataIngressConfsRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('SslRedirect') is not None:
            self.ssl_redirect = m.get('SslRedirect')

        return self

class ListK8sIngressRulesResponseBodyDataIngressConfsRules(DaraModel):
    def __init__(
        self,
        enable_tls: bool = None,
        host: str = None,
        paths: List[main_models.ListK8sIngressRulesResponseBodyDataIngressConfsRulesPaths] = None,
        secret_name: str = None,
    ):
        # Indicates whether TLS is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.enable_tls = enable_tls
        # The domain name to be accessed.
        self.host = host
        # The paths to be accessed.
        self.paths = paths
        # The name of the Secret that stores the Transport Layer Security (TLS) certificate.
        self.secret_name = secret_name

    def validate(self):
        if self.paths:
            for v1 in self.paths:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_tls is not None:
            result['EnableTls'] = self.enable_tls

        if self.host is not None:
            result['Host'] = self.host

        result['Paths'] = []
        if self.paths is not None:
            for k1 in self.paths:
                result['Paths'].append(k1.to_map() if k1 else None)

        if self.secret_name is not None:
            result['SecretName'] = self.secret_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableTls') is not None:
            self.enable_tls = m.get('EnableTls')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        self.paths = []
        if m.get('Paths') is not None:
            for k1 in m.get('Paths'):
                temp_model = main_models.ListK8sIngressRulesResponseBodyDataIngressConfsRulesPaths()
                self.paths.append(temp_model.from_map(k1))

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        return self

class ListK8sIngressRulesResponseBodyDataIngressConfsRulesPaths(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        backend: main_models.ListK8sIngressRulesResponseBodyDataIngressConfsRulesPathsBackend = None,
        collect_rate: int = None,
        path: str = None,
        path_type: str = None,
        status: str = None,
    ):
        # The ID of the EDAS application.
        self.app_id = app_id
        # The name of the EDAS application.
        self.app_name = app_name
        # The configurations of the backend Service.
        self.backend = backend
        # The collection rate that is set based on the trace query feature. You can add a trace ID to a gateway to use the trace query feature of EDAS.
        self.collect_rate = collect_rate
        # The path to be accessed.
        self.path = path
        # The path type that determines how a path is matched.
        # 
        # *   ImplementationSpecific (default)
        # *   Exact
        # *   Prefix
        self.path_type = path_type
        # The state of the Ingress. Valid values:
        # 
        # *   **Normal**: The Ingress works as expected.
        # *   **ServiceNotFound**: The backend Service does not exist.
        # *   **InvalidServicePort**: The Service port is invalid.
        # *   **NotManagedService**: The Service is not managed by EDAS.
        # *   **Unknown**: An unknown error occurred.
        self.status = status

    def validate(self):
        if self.backend:
            self.backend.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.backend is not None:
            result['Backend'] = self.backend.to_map()

        if self.collect_rate is not None:
            result['CollectRate'] = self.collect_rate

        if self.path is not None:
            result['Path'] = self.path

        if self.path_type is not None:
            result['PathType'] = self.path_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Backend') is not None:
            temp_model = main_models.ListK8sIngressRulesResponseBodyDataIngressConfsRulesPathsBackend()
            self.backend = temp_model.from_map(m.get('Backend'))

        if m.get('CollectRate') is not None:
            self.collect_rate = m.get('CollectRate')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('PathType') is not None:
            self.path_type = m.get('PathType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListK8sIngressRulesResponseBodyDataIngressConfsRulesPathsBackend(DaraModel):
    def __init__(
        self,
        service_name: str = None,
        service_port: str = None,
    ):
        # The name of the backend Service.
        self.service_name = service_name
        # The port of the backend Service.
        self.service_port = service_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_port is not None:
            result['ServicePort'] = self.service_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServicePort') is not None:
            self.service_port = m.get('ServicePort')

        return self

