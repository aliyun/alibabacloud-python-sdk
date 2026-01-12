# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckModifyConfigNeedRestartResponseBody(DaraModel):
    def __init__(
        self,
        need_restart: bool = None,
        request_id: str = None,
    ):
        # Indicates whether the cluster was restarted after you modified the configuration parameters. Valid values:
        # 
        # *   **true**: The cluster was restarted.
        # *   **false**: The cluster was not restarted.
        self.need_restart = need_restart
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.need_restart is not None:
            result['NeedRestart'] = self.need_restart

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NeedRestart') is not None:
            self.need_restart = m.get('NeedRestart')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

