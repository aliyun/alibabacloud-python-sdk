# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class ListDataSourceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListDataSourceResponseBodyResult] = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Array of data source information.
        self.result = result
        # Whether the request was successful.
        self.success = success

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListDataSourceResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDataSourceResponseBodyResult(DaraModel):
    def __init__(
        self,
        creator_id: str = None,
        creator_name: str = None,
        datasource_id: str = None,
        ds_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        parent_ds_type: str = None,
        show_name: str = None,
    ):
        # Quick BI user ID of the creator.
        self.creator_id = creator_id
        # Owner\\"s nickname.
        self.creator_name = creator_name
        # Data source ID.
        self.datasource_id = datasource_id
        # Data source type.
        self.ds_type = ds_type
        # Creation time of the data source, in yyyy-MM-dd HH:mm:ss format.
        self.gmt_create = gmt_create
        # Modification time.
        self.gmt_modified = gmt_modified
        # Primary data source type for multi-engine data sources.
        self.parent_ds_type = parent_ds_type
        # Display name of the data source.
        self.show_name = show_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id

        if self.ds_type is not None:
            result['DsType'] = self.ds_type

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.parent_ds_type is not None:
            result['ParentDsType'] = self.parent_ds_type

        if self.show_name is not None:
            result['ShowName'] = self.show_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')

        if m.get('DsType') is not None:
            self.ds_type = m.get('DsType')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('ParentDsType') is not None:
            self.parent_ds_type = m.get('ParentDsType')

        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')

        return self

