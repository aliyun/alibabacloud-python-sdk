# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddDataSourceRequest(DaraModel):
    def __init__(
        self,
        add_model: str = None,
    ):
        # To construct the request payload, you can replicate the add data source process in the Quick BI console. On the Add Data Source page, when you click Test Connection, the restapi/datasource/detect API is called. Use this API call\\"s payload as a template, ensuring that the provided userId and workspaceId exist in your Quick BI environment.
        # >Notice: A few data source types are not supported. If your parameters match the test API request payload but the request still fails, the data source type is likely not supported by this OpenAPI.
        # >Notice: Do not include the `encode` field in your request. This API does not support creating data sources in encrypted mode or using authentication methods that require file uploads.
        # 
        # This parameter is required.
        self.add_model = add_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_model is not None:
            result['AddModel'] = self.add_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddModel') is not None:
            self.add_model = m.get('AddModel')

        return self

