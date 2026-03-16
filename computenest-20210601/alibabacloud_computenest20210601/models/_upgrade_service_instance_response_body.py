# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpgradeServiceInstanceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        upgrade_required_parameters: List[str] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The parameters required for the upgrade. This parameter is returned only if DryRun is set to true in the request. You can specify the required parameters based on the returned value when you perform an actual request.
        self.upgrade_required_parameters = upgrade_required_parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.upgrade_required_parameters is not None:
            result['UpgradeRequiredParameters'] = self.upgrade_required_parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UpgradeRequiredParameters') is not None:
            self.upgrade_required_parameters = m.get('UpgradeRequiredParameters')

        return self

