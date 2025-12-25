# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DeleteBackupFileResponseBody(DaraModel):
    def __init__(
        self,
        deleted_bakset_ids: main_models.DeleteBackupFileResponseBodyDeletedBaksetIds = None,
        request_id: str = None,
    ):
        # An array that consists of the IDs of deleted backup sets.
        self.deleted_bakset_ids = deleted_bakset_ids
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.deleted_bakset_ids:
            self.deleted_bakset_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deleted_bakset_ids is not None:
            result['DeletedBaksetIds'] = self.deleted_bakset_ids.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletedBaksetIds') is not None:
            temp_model = main_models.DeleteBackupFileResponseBodyDeletedBaksetIds()
            self.deleted_bakset_ids = temp_model.from_map(m.get('DeletedBaksetIds'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DeleteBackupFileResponseBodyDeletedBaksetIds(DaraModel):
    def __init__(
        self,
        deleted_bakset_ids: List[int] = None,
    ):
        self.deleted_bakset_ids = deleted_bakset_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deleted_bakset_ids is not None:
            result['DeletedBaksetIds'] = self.deleted_bakset_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletedBaksetIds') is not None:
            self.deleted_bakset_ids = m.get('DeletedBaksetIds')

        return self

