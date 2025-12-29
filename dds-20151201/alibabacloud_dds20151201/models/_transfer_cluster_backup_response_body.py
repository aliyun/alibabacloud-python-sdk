# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TransferClusterBackupResponseBody(DaraModel):
    def __init__(
        self,
        already_done: str = None,
        request_id: str = None,
    ):
        # Indicates whether the instance is switched to the cluster backup mode. If the value of this parameter is **1**, the instance is switched to the cluster backup mode.
        self.already_done = already_done
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.already_done is not None:
            result['AlreadyDone'] = self.already_done

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlreadyDone') is not None:
            self.already_done = m.get('AlreadyDone')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

