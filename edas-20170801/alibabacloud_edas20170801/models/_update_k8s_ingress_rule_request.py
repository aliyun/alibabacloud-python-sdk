# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class UpdateK8sIngressRuleRequest(DaraModel):
    def __init__(
        self,
        annotations: str = None,
        cluster_id: str = None,
        ingress_conf: Dict[str, Any] = None,
        labels: str = None,
        name: str = None,
        namespace: str = None,
    ):
        # The annotations.
        self.annotations = annotations
        # The ID of the Kubernetes cluster.
        self.cluster_id = cluster_id
        # The routing rules of the Ingress. Set this parameter to a JSON string in the following format:
        # 
        #     {
        #       "rules": [
        #         {
        #           "host": "abc.com",
        #           "secretName": "tls-secret",
        #           "paths": [
        #             {
        #               "path": "/path",
        #               "backend": {
        #                 "servicePort": 80,
        #                 "serviceName": "xxx"
        #               }
        #             }
        #           ]
        #         }
        #       ]
        #     }
        # 
        # Parameter description:
        # 
        # *   rules: the list of routing rules.
        # *   host: the domain name to be accessed.
        # *   secretName: the name of the Secret that stores the information about the Transport Layer Security (TLS) certificate. The certificate is required if you need to use the HTTPS protocol.
        # *   paths: the list of paths to be accessed.
        # *   path: the path to be accessed.
        # *   backend: the configuration of the backend service. You can specify a service that is created in the Enterprise Distributed Application Service (EDAS) console.
        # *   serviceName: the name of the backend service.
        # *   servicePort: the port of the backend service.
        self.ingress_conf = ingress_conf
        # The labels.
        self.labels = labels
        # The name of the Ingress. The name can contain lowercase letters, digits, and hyphens (-). It must start with a lowercase letter but cannot end with a hyphen (-). The name can be up to 63 characters in length.
        self.name = name
        # The namespace of the Kubernetes cluster.
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotations is not None:
            result['Annotations'] = self.annotations

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.ingress_conf is not None:
            result['IngressConf'] = self.ingress_conf

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('IngressConf') is not None:
            self.ingress_conf = m.get('IngressConf')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        return self

