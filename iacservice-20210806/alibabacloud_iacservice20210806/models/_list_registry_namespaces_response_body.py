# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class ListRegistryNamespacesResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        max_results: int = None,
        namespaces: List[main_models.ListRegistryNamespacesResponseBodyNamespaces] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.count = count
        self.max_results = max_results
        self.namespaces = namespaces
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.namespaces:
            for v1 in self.namespaces:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['count'] = self.count

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        result['namespaces'] = []
        if self.namespaces is not None:
            for k1 in self.namespaces:
                result['namespaces'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        self.namespaces = []
        if m.get('namespaces') is not None:
            for k1 in m.get('namespaces'):
                temp_model = main_models.ListRegistryNamespacesResponseBodyNamespaces()
                self.namespaces.append(temp_model.from_map(k1))

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListRegistryNamespacesResponseBodyNamespaces(DaraModel):
    def __init__(
        self,
        acl: str = None,
        create_time: str = None,
        description: str = None,
        maintainer: str = None,
        modules: int = None,
        namespace_name: str = None,
        shared_accounts: List[int] = None,
        type: str = None,
    ):
        self.acl = acl
        self.create_time = create_time
        self.description = description
        self.maintainer = maintainer
        self.modules = modules
        self.namespace_name = namespace_name
        self.shared_accounts = shared_accounts
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl is not None:
            result['acl'] = self.acl

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.maintainer is not None:
            result['maintainer'] = self.maintainer

        if self.modules is not None:
            result['modules'] = self.modules

        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name

        if self.shared_accounts is not None:
            result['sharedAccounts'] = self.shared_accounts

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acl') is not None:
            self.acl = m.get('acl')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('maintainer') is not None:
            self.maintainer = m.get('maintainer')

        if m.get('modules') is not None:
            self.modules = m.get('modules')

        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')

        if m.get('sharedAccounts') is not None:
            self.shared_accounts = m.get('sharedAccounts')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

