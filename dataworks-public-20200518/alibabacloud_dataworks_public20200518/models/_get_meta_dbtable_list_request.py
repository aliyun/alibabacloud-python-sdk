# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMetaDBTableListRequest(DaraModel):
    def __init__(
        self,
        app_guid: str = None,
        cluster_id: str = None,
        data_source_type: str = None,
        database_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The GUID of the MaxCompute project. Specify the GUID in the `odps.{projectName}` format. You must configure this parameter only if you set the DataSourceType parameter to odps.
        self.app_guid = app_guid
        # The E-MapReduce (EMR) cluster ID. You must configure this parameter only if you set the DataSourceType parameter to emr.
        self.cluster_id = cluster_id
        # The type of the data source. Valid values: odps and emr.
        self.data_source_type = data_source_type
        # The name of the metadatabase.
        self.database_name = database_name
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_guid is not None:
            result['AppGuid'] = self.app_guid

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppGuid') is not None:
            self.app_guid = m.get('AppGuid')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

