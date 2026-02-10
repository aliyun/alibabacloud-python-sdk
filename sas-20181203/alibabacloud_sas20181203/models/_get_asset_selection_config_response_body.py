# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetAssetSelectionConfigResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetAssetSelectionConfigResponseBodyData = None,
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
            temp_model = main_models.GetAssetSelectionConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAssetSelectionConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        platform: str = None,
        selection_key: str = None,
        target_type: str = None,
    ):
        # The operating system of the asset. Valid values:
        # 
        # *   **windows**
        # *   **linux**
        self.platform = platform
        # The ID of the current asset selection. It can be used to query and modify the asset that is selected.
        self.selection_key = selection_key
        # The dimension based on which the asset is selected. Valid values:
        # 
        # *   **instance**: The asset is selected by server.
        # *   **group**: The asset is selected by group.
        # *   **vpc**: The asset is selected by VPC.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.platform is not None:
            result['Platform'] = self.platform

        if self.selection_key is not None:
            result['SelectionKey'] = self.selection_key

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('SelectionKey') is not None:
            self.selection_key = m.get('SelectionKey')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

