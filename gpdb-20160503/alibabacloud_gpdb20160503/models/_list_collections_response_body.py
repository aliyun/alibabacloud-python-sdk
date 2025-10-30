# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ListCollectionsResponseBody(DaraModel):
    def __init__(
        self,
        collections: main_models.ListCollectionsResponseBodyCollections = None,
        count: int = None,
        dbinstance_id: str = None,
        message: str = None,
        namespace: str = None,
        region_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The queried vector collections.
        self.collections = collections
        # The total number of entries returned.
        self.count = count
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The returned message.
        self.message = message
        # The name of the namespace.
        self.namespace = namespace
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
        if self.collections:
            self.collections.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collections is not None:
            result['Collections'] = self.collections.to_map()

        if self.count is not None:
            result['Count'] = self.count

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.message is not None:
            result['Message'] = self.message

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collections') is not None:
            temp_model = main_models.ListCollectionsResponseBodyCollections()
            self.collections = temp_model.from_map(m.get('Collections'))

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListCollectionsResponseBodyCollections(DaraModel):
    def __init__(
        self,
        collection: List[str] = None,
    ):
        self.collection = collection

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collection is not None:
            result['Collection'] = self.collection

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')

        return self

