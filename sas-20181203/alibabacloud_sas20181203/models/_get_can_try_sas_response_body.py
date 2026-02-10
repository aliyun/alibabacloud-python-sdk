# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetCanTrySasResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetCanTrySasResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetCanTrySasResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetCanTrySasResponseBodyData(DaraModel):
    def __init__(
        self,
        can_try: int = None,
        can_try_versions: List[int] = None,
        try_type: int = None,
    ):
        # Indicates whether the user is qualified for the trial use. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.can_try = can_try
        # The editions that are allowed for the trial use.
        self.can_try_versions = can_try_versions
        # The trial type. Valid values:
        # 
        # *   **0**: trial prohibited
        # *   **1**: first trial
        # *   **2**: second trial
        self.try_type = try_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_try is not None:
            result['CanTry'] = self.can_try

        if self.can_try_versions is not None:
            result['CanTryVersions'] = self.can_try_versions

        if self.try_type is not None:
            result['TryType'] = self.try_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanTry') is not None:
            self.can_try = m.get('CanTry')

        if m.get('CanTryVersions') is not None:
            self.can_try_versions = m.get('CanTryVersions')

        if m.get('TryType') is not None:
            self.try_type = m.get('TryType')

        return self

