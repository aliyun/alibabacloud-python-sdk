# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeComponentAssetFormResponseBody(DaraModel):
    def __init__(
        self,
        component_asset_form: str = None,
        request_id: str = None,
    ):
        # The metadata of the asset in the component. The value is a JSON array and contains the following fields:
        # 
        # *   **name**: the parameter name.
        # *   **defaultValue**: the default parameter value.
        # *   **description**: the parameter description.
        # *   **required**: indicates whether the parameter is required. Valid values: **true** and **false**.
        self.component_asset_form = component_asset_form
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_asset_form is not None:
            result['ComponentAssetForm'] = self.component_asset_form

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentAssetForm') is not None:
            self.component_asset_form = m.get('ComponentAssetForm')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

