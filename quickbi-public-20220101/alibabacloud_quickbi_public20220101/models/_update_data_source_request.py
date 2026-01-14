# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDataSourceRequest(DaraModel):
    def __init__(
        self,
        update_model: str = None,
    ):
        # Refer to the example JSON for parameter values. The parameters are explained as follows:
        # 
        # - dsId  --  Required  --  Data source ID
        # - userId -- Optional -- User identity for modifying the data source, quickbi\\"s userId. If provided, it will use the current userId for modification.
        # - dsType -- Required -- Data source type, not allowed to be modified, just pass the data source type.
        # - showName -- Optional -- Display name of the data source.
        # - address -- Optional -- Database connection string (domain or IP)
        # - port -- Optional -- Port
        # - schema --  Optional --  Database schema, only required for databases that support schemas. Example: sqlserver uses dbo by default; mysql does not support schemas.
        # - instance -- Optional -- Instance db
        # - username -- Optional -- Database username/ak
        # - password -- Optional -- Database key
        # - config -- Optional -- Additional database configuration items. Note that this data should be consistent with the different config parameters passed during creation for different data sources. Fields that do not need to be modified do not require parameters. For fields where parameters are passed, the default is to modify according to the passed parameters (including empty strings).
        # 
        # This parameter is required.
        self.update_model = update_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.update_model is not None:
            result['UpdateModel'] = self.update_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateModel') is not None:
            self.update_model = m.get('UpdateModel')

        return self

