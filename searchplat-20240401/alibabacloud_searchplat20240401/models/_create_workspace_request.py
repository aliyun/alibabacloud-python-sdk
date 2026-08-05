# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_searchplat20240401 import models as main_models
from darabonba.model import DaraModel

class CreateWorkspaceRequest(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        engine_type: str = None,
        name: str = None,
        quota: main_models.CreateWorkspaceRequestQuota = None,
        type: str = None,
    ):
        # Billing type
        # - POSTPAY: Pay-as-you-go
        self.charge_type = charge_type
        # Engine type
        # - rag
        self.engine_type = engine_type
        # Workspace name
        self.name = name
        # Quota
        self.quota = quota
        # Type
        # - standard
        self.type = type

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type

        if self.engine_type is not None:
            result['engineType'] = self.engine_type

        if self.name is not None:
            result['name'] = self.name

        if self.quota is not None:
            result['quota'] = self.quota.to_map()

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')

        if m.get('engineType') is not None:
            self.engine_type = m.get('engineType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('quota') is not None:
            temp_model = main_models.CreateWorkspaceRequestQuota()
            self.quota = temp_model.from_map(m.get('quota'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateWorkspaceRequestQuota(DaraModel):
    def __init__(
        self,
        compute_resource: int = None,
        doc_size: int = None,
        spec: str = None,
    ):
        # Compute resource (unit: LCU)
        self.compute_resource = compute_resource
        # Storage capacity (unit: GB)
        self.doc_size = doc_size
        # Specification
        # - rag.share.common
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource

        if self.doc_size is not None:
            result['docSize'] = self.doc_size

        if self.spec is not None:
            result['spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')

        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        return self

