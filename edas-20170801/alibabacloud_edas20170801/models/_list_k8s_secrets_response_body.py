# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class ListK8sSecretsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.ListK8sSecretsResponseBodyResult = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The additional information that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The returned query results of Kubernetes Secrets.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.ListK8sSecretsResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class ListK8sSecretsResponseBodyResult(DaraModel):
    def __init__(
        self,
        secrets: List[main_models.ListK8sSecretsResponseBodyResultSecrets] = None,
        total: int = None,
    ):
        # The information about Kubernetes Secrets.
        self.secrets = secrets
        # The total number of entries that are returned.
        self.total = total

    def validate(self):
        if self.secrets:
            for v1 in self.secrets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Secrets'] = []
        if self.secrets is not None:
            for k1 in self.secrets:
                result['Secrets'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.secrets = []
        if m.get('Secrets') is not None:
            for k1 in m.get('Secrets'):
                temp_model = main_models.ListK8sSecretsResponseBodyResultSecrets()
                self.secrets.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListK8sSecretsResponseBodyResultSecrets(DaraModel):
    def __init__(
        self,
        base_64encoded: bool = None,
        cert_detail: main_models.ListK8sSecretsResponseBodyResultSecretsCertDetail = None,
        cert_id: str = None,
        cert_region_id: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        creation_time: str = None,
        data: List[main_models.ListK8sSecretsResponseBodyResultSecretsData] = None,
        name: str = None,
        namespace: str = None,
        related_apps: List[main_models.ListK8sSecretsResponseBodyResultSecretsRelatedApps] = None,
        related_ingress_rules: List[main_models.ListK8sSecretsResponseBodyResultSecretsRelatedIngressRules] = None,
        type: str = None,
    ):
        # Indicates whether the data is Base64-encoded. Valid values:
        # 
        # - true: The data is Base64-encoded.
        # 
        # - false: The data is not Base64-encoded.
        self.base_64encoded = base_64encoded
        # The details of the Secure Sockets Layer (SSL) certificate.
        self.cert_detail = cert_detail
        # The ID of the certificate provided by Alibaba Cloud Certificate Management Service.
        self.cert_id = cert_id
        # The region in which the certificate is stored.
        self.cert_region_id = cert_region_id
        # The ID of the cluster in Enterprise Distributed Application Service (EDAS).
        self.cluster_id = cluster_id
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The time when the Secret was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*hh:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The data of the Kubernetes Secret.
        self.data = data
        # The name of the Secret. The name must start with a letter, and can contain digits, letters, and hyphens (-). It can be up to 63 characters in length.
        self.name = name
        # The namespace of the Kubernetes cluster.
        self.namespace = namespace
        # Applications that use the Secret.
        self.related_apps = related_apps
        # Rules in the Ingress that is associated with the Secret.
        self.related_ingress_rules = related_ingress_rules
        # The type of the Secret. Valid values:
        # 
        # - Opaque: user-defined data
        # 
        # - kubernetes.io/tls: Transport Layer Security (TLS) certificate
        self.type = type

    def validate(self):
        if self.cert_detail:
            self.cert_detail.validate()
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()
        if self.related_apps:
            for v1 in self.related_apps:
                 if v1:
                    v1.validate()
        if self.related_ingress_rules:
            for v1 in self.related_ingress_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_64encoded is not None:
            result['Base64Encoded'] = self.base_64encoded

        if self.cert_detail is not None:
            result['CertDetail'] = self.cert_detail.to_map()

        if self.cert_id is not None:
            result['CertId'] = self.cert_id

        if self.cert_region_id is not None:
            result['CertRegionId'] = self.cert_region_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        result['RelatedApps'] = []
        if self.related_apps is not None:
            for k1 in self.related_apps:
                result['RelatedApps'].append(k1.to_map() if k1 else None)

        result['RelatedIngressRules'] = []
        if self.related_ingress_rules is not None:
            for k1 in self.related_ingress_rules:
                result['RelatedIngressRules'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Base64Encoded') is not None:
            self.base_64encoded = m.get('Base64Encoded')

        if m.get('CertDetail') is not None:
            temp_model = main_models.ListK8sSecretsResponseBodyResultSecretsCertDetail()
            self.cert_detail = temp_model.from_map(m.get('CertDetail'))

        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        if m.get('CertRegionId') is not None:
            self.cert_region_id = m.get('CertRegionId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListK8sSecretsResponseBodyResultSecretsData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        self.related_apps = []
        if m.get('RelatedApps') is not None:
            for k1 in m.get('RelatedApps'):
                temp_model = main_models.ListK8sSecretsResponseBodyResultSecretsRelatedApps()
                self.related_apps.append(temp_model.from_map(k1))

        self.related_ingress_rules = []
        if m.get('RelatedIngressRules') is not None:
            for k1 in m.get('RelatedIngressRules'):
                temp_model = main_models.ListK8sSecretsResponseBodyResultSecretsRelatedIngressRules()
                self.related_ingress_rules.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListK8sSecretsResponseBodyResultSecretsRelatedIngressRules(DaraModel):
    def __init__(
        self,
        name: str = None,
        namespace: str = None,
        related_apps: List[main_models.ListK8sSecretsResponseBodyResultSecretsRelatedIngressRulesRelatedApps] = None,
    ):
        # The name of the rule in the Ingress.
        self.name = name
        # The namespaces of the Kubernetes cluster.
        self.namespace = namespace
        # Aplications that are associated with the Ingress.
        self.related_apps = related_apps

    def validate(self):
        if self.related_apps:
            for v1 in self.related_apps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        result['RelatedApps'] = []
        if self.related_apps is not None:
            for k1 in self.related_apps:
                result['RelatedApps'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        self.related_apps = []
        if m.get('RelatedApps') is not None:
            for k1 in m.get('RelatedApps'):
                temp_model = main_models.ListK8sSecretsResponseBodyResultSecretsRelatedIngressRulesRelatedApps()
                self.related_apps.append(temp_model.from_map(k1))

        return self

class ListK8sSecretsResponseBodyResultSecretsRelatedIngressRulesRelatedApps(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The name of the EDAS application.
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        return self

class ListK8sSecretsResponseBodyResultSecretsRelatedApps(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        return self

class ListK8sSecretsResponseBodyResultSecretsData(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The user-defined key of the Kubernetes Secret.
        self.key = key
        # The user-defined value of the Kubernetes Secret.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class ListK8sSecretsResponseBodyResultSecretsCertDetail(DaraModel):
    def __init__(
        self,
        domain_names: List[str] = None,
        end_time: str = None,
        issuer: str = None,
        start_time: str = None,
        status: str = None,
    ):
        # Domain names that are associated with the SSL certificate.
        self.domain_names = domain_names
        # The time when the SSL certificate expired.
        self.end_time = end_time
        # The certificate authority (CA) that issued the SSL certificate.
        self.issuer = issuer
        # The time when the SSL certificate started to take effect.
        self.start_time = start_time
        # The state of the SSL certificate. Valid values:
        # 
        # - normal: The SSL certificate is valid.
        # 
        # - invalid: The SSL certificate is invalid.
        # 
        # - expired: The SSL certificate has expired.
        # 
        # - not_yet_valid: The SSL certificate is currently invalid.
        # 
        # - about_to_expire: The SSL certificate is about to expire.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

