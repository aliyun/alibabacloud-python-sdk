# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddDataSourceRequest(DaraModel):
    def __init__(
        self,
        add_model: str = None,
    ):
        # You can refer to the logic of adding a data source on the Quick BI data source page. When you click **Test Connection**, the `restapi/datasource/detect` API operation is triggered. Simulate the request payload of this API operation by passing a JSON object of the same model, along with a valid `userId` and workspace ID in Quick BI. In version 7.1, the `userAsOwner` parameter is added. If you set this parameter to true, the data source is created as the specified `userId`.
        # <notice>A small number of data sources are not supported. If the parameters are the same as the request payload of the test API operation but the data source still fails to be added, the current data source type does not support creation through this API operation.</notice>
        # <notice>Do not pass the `encode` parameter. Currently, this API operation does not support encryption mode for creating data sources, and authentication that involves uploading files is not supported.</notice>
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

