# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_foasconsole20190601 import models as main_models
from darabonba.model import DaraModel

class DeleteNamespaceRequest(DaraModel):
    def __init__(
        self,
        delete_namespace_request: main_models.DeleteNamespaceRequestDeleteNamespaceRequest = None,
    ):
        # This parameter is required.
        self.delete_namespace_request = delete_namespace_request

    def validate(self):
        if self.delete_namespace_request:
            self.delete_namespace_request.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_namespace_request is not None:
            result['DeleteNamespaceRequest'] = self.delete_namespace_request.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteNamespaceRequest') is not None:
            temp_model = main_models.DeleteNamespaceRequestDeleteNamespaceRequest()
            self.delete_namespace_request = temp_model.from_map(m.get('DeleteNamespaceRequest'))

        return self

class DeleteNamespaceRequestDeleteNamespaceRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        namespace: str = None,
        region: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.namespace = namespace
        # This parameter is required.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

