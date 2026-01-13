# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartProcessInstanceRequest(DaraModel):
    def __init__(
        self,
        action: str = None,
        comments: str = None,
        email: str = None,
        interval: str = None,
        is_prod: bool = None,
        process_definition_code: int = None,
        product_namespace: str = None,
        region_id: str = None,
        runtime_queue: str = None,
        version_hash_code: str = None,
        version_number: int = None,
    ):
        self.action = action
        self.comments = comments
        self.email = email
        self.interval = interval
        # Specifies whether to run the workflow in the production environment.
        self.is_prod = is_prod
        # The workflow ID.
        # 
        # This parameter is required.
        self.process_definition_code = process_definition_code
        # The code of the service.
        # 
        # This parameter is required.
        self.product_namespace = product_namespace
        # The region ID.
        self.region_id = region_id
        # The queue on which the workflow runs.
        self.runtime_queue = runtime_queue
        # The hash code of the version.
        self.version_hash_code = version_hash_code
        # The version number of the workflow.
        self.version_number = version_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.comments is not None:
            result['comments'] = self.comments

        if self.email is not None:
            result['email'] = self.email

        if self.interval is not None:
            result['interval'] = self.interval

        if self.is_prod is not None:
            result['isProd'] = self.is_prod

        if self.process_definition_code is not None:
            result['processDefinitionCode'] = self.process_definition_code

        if self.product_namespace is not None:
            result['productNamespace'] = self.product_namespace

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.runtime_queue is not None:
            result['runtimeQueue'] = self.runtime_queue

        if self.version_hash_code is not None:
            result['versionHashCode'] = self.version_hash_code

        if self.version_number is not None:
            result['versionNumber'] = self.version_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('comments') is not None:
            self.comments = m.get('comments')

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('interval') is not None:
            self.interval = m.get('interval')

        if m.get('isProd') is not None:
            self.is_prod = m.get('isProd')

        if m.get('processDefinitionCode') is not None:
            self.process_definition_code = m.get('processDefinitionCode')

        if m.get('productNamespace') is not None:
            self.product_namespace = m.get('productNamespace')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('runtimeQueue') is not None:
            self.runtime_queue = m.get('runtimeQueue')

        if m.get('versionHashCode') is not None:
            self.version_hash_code = m.get('versionHashCode')

        if m.get('versionNumber') is not None:
            self.version_number = m.get('versionNumber')

        return self

