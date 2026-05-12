# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class ListClusterAddonInstanceResourcesResponseBody(DaraModel):
    def __init__(
        self,
        helm_release: main_models.ListClusterAddonInstanceResourcesResponseBodyHelmRelease = None,
        kubernetes_objects: List[main_models.ListClusterAddonInstanceResourcesResponseBodyKubernetesObjects] = None,
    ):
        # Information about the Helm release instance corresponding to the add-on.
        self.helm_release = helm_release
        # A list of Kubernetes objects associated with the add-on.
        self.kubernetes_objects = kubernetes_objects

    def validate(self):
        if self.helm_release:
            self.helm_release.validate()
        if self.kubernetes_objects:
            for v1 in self.kubernetes_objects:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.helm_release is not None:
            result['helm_release'] = self.helm_release.to_map()

        result['kubernetes_objects'] = []
        if self.kubernetes_objects is not None:
            for k1 in self.kubernetes_objects:
                result['kubernetes_objects'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('helm_release') is not None:
            temp_model = main_models.ListClusterAddonInstanceResourcesResponseBodyHelmRelease()
            self.helm_release = temp_model.from_map(m.get('helm_release'))

        self.kubernetes_objects = []
        if m.get('kubernetes_objects') is not None:
            for k1 in m.get('kubernetes_objects'):
                temp_model = main_models.ListClusterAddonInstanceResourcesResponseBodyKubernetesObjects()
                self.kubernetes_objects.append(temp_model.from_map(k1))

        return self

class ListClusterAddonInstanceResourcesResponseBodyKubernetesObjects(DaraModel):
    def __init__(
        self,
        group: str = None,
        kind: str = None,
        name: str = None,
        namespace: str = None,
        version: str = None,
    ):
        # The Kubernetes API group to which the object belongs.
        self.group = group
        # The Kubernetes API type to which the object belongs.
        self.kind = kind
        # The name of the Kubernetes object.
        self.name = name
        # The namespace to which the object belongs.
        self.namespace = namespace
        # The Kubernetes API version to which the object belongs.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group is not None:
            result['group'] = self.group

        if self.kind is not None:
            result['kind'] = self.kind

        if self.name is not None:
            result['name'] = self.name

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group') is not None:
            self.group = m.get('group')

        if m.get('kind') is not None:
            self.kind = m.get('kind')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class ListClusterAddonInstanceResourcesResponseBodyHelmRelease(DaraModel):
    def __init__(
        self,
        chart_name: str = None,
        chart_version: str = None,
        namespace: str = None,
        release_name: str = None,
    ):
        # The name of the Helm chart.
        self.chart_name = chart_name
        # The version of the Helm chart.
        self.chart_version = chart_version
        # The namespace where the Helm release is located.
        self.namespace = namespace
        # The name of the Helm release instance.
        self.release_name = release_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chart_name is not None:
            result['chart_name'] = self.chart_name

        if self.chart_version is not None:
            result['chart_version'] = self.chart_version

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.release_name is not None:
            result['release_name'] = self.release_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chart_name') is not None:
            self.chart_name = m.get('chart_name')

        if m.get('chart_version') is not None:
            self.chart_version = m.get('chart_version')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('release_name') is not None:
            self.release_name = m.get('release_name')

        return self

