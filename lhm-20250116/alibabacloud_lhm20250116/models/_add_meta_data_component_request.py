# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddMetaDataComponentRequest(DaraModel):
    def __init__(
        self,
        category_type: str = None,
        component_type: int = None,
        ds_config: str = None,
        ds_desc: str = None,
        ds_id: str = None,
        ds_name: str = None,
        ds_status: int = None,
        ds_type: str = None,
        ds_version: str = None,
    ):
        # The data source category. Valid values: DATASET, WORKFLOW, ENGINE.
        self.category_type = category_type
        # The role of the data source in the migration pipeline. Valid values:
        # - 0: source.
        # - 1: destination.
        self.component_type = component_type
        # The datasource config.
        self.ds_config = ds_config
        # The description of the data source.
        self.ds_desc = ds_desc
        # The external ID of the data source.
        self.ds_id = ds_id
        # The name of the data source.
        self.ds_name = ds_name
        # The connectivity status of the data source.
        self.ds_status = ds_status
        # The type of the data source.
        self.ds_type = ds_type
        # The version of the data source.
        self.ds_version = ds_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_type is not None:
            result['categoryType'] = self.category_type

        if self.component_type is not None:
            result['componentType'] = self.component_type

        if self.ds_config is not None:
            result['dsConfig'] = self.ds_config

        if self.ds_desc is not None:
            result['dsDesc'] = self.ds_desc

        if self.ds_id is not None:
            result['dsId'] = self.ds_id

        if self.ds_name is not None:
            result['dsName'] = self.ds_name

        if self.ds_status is not None:
            result['dsStatus'] = self.ds_status

        if self.ds_type is not None:
            result['dsType'] = self.ds_type

        if self.ds_version is not None:
            result['dsVersion'] = self.ds_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('categoryType') is not None:
            self.category_type = m.get('categoryType')

        if m.get('componentType') is not None:
            self.component_type = m.get('componentType')

        if m.get('dsConfig') is not None:
            self.ds_config = m.get('dsConfig')

        if m.get('dsDesc') is not None:
            self.ds_desc = m.get('dsDesc')

        if m.get('dsId') is not None:
            self.ds_id = m.get('dsId')

        if m.get('dsName') is not None:
            self.ds_name = m.get('dsName')

        if m.get('dsStatus') is not None:
            self.ds_status = m.get('dsStatus')

        if m.get('dsType') is not None:
            self.ds_type = m.get('dsType')

        if m.get('dsVersion') is not None:
            self.ds_version = m.get('dsVersion')

        return self

