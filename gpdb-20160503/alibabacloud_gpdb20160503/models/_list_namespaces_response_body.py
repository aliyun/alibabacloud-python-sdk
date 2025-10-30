# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ListNamespacesResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        dbinstance_id: str = None,
        message: str = None,
        namespaces: main_models.ListNamespacesResponseBodyNamespaces = None,
        region_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The total number of entries returned.
        self.count = count
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The returned message.
        self.message = message
        # The queried namespaces.
        self.namespaces = namespaces
        # The region ID of the instance.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **success**
        # *   **fail**
        self.status = status

    def validate(self):
        if self.namespaces:
            self.namespaces.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.message is not None:
            result['Message'] = self.message

        if self.namespaces is not None:
            result['Namespaces'] = self.namespaces.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Namespaces') is not None:
            temp_model = main_models.ListNamespacesResponseBodyNamespaces()
            self.namespaces = temp_model.from_map(m.get('Namespaces'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListNamespacesResponseBodyNamespaces(DaraModel):
    def __init__(
        self,
        namespace: List[str] = None,
    ):
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.namespace is not None:
            result['Namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        return self

