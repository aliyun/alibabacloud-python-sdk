# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteVerifyResultRequest(DaraModel):
    def __init__(
        self,
        delete_after_query: str = None,
        delete_type: str = None,
        transaction_id: str = None,
    ):
        # Whether to depend on the query interface when deleting data
        self.delete_after_query = delete_after_query
        # Type of data to be deleted
        self.delete_type = delete_type
        # Unique identifier of the authentication request
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_after_query is not None:
            result['DeleteAfterQuery'] = self.delete_after_query

        if self.delete_type is not None:
            result['DeleteType'] = self.delete_type

        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteAfterQuery') is not None:
            self.delete_after_query = m.get('DeleteAfterQuery')

        if m.get('DeleteType') is not None:
            self.delete_type = m.get('DeleteType')

        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')

        return self

