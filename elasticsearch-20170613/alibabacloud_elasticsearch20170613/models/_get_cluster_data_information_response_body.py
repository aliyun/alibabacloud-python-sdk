# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class GetClusterDataInformationResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.GetClusterDataInformationResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The return results.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetClusterDataInformationResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class GetClusterDataInformationResponseBodyResult(DaraModel):
    def __init__(
        self,
        connectable: bool = None,
        meta_info: main_models.GetClusterDataInformationResponseBodyResultMetaInfo = None,
    ):
        # Whether it is connectable.
        self.connectable = connectable
        # The metadata of the cluster.
        self.meta_info = meta_info

    def validate(self):
        if self.meta_info:
            self.meta_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connectable is not None:
            result['connectable'] = self.connectable

        if self.meta_info is not None:
            result['metaInfo'] = self.meta_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('connectable') is not None:
            self.connectable = m.get('connectable')

        if m.get('metaInfo') is not None:
            temp_model = main_models.GetClusterDataInformationResponseBodyResultMetaInfo()
            self.meta_info = temp_model.from_map(m.get('metaInfo'))

        return self

class GetClusterDataInformationResponseBodyResultMetaInfo(DaraModel):
    def __init__(
        self,
        fields: List[str] = None,
        indices: List[str] = None,
        mapping: str = None,
        settings: str = None,
        type_name: List[str] = None,
    ):
        # The fields in the Mapping for the index.
        self.fields = fields
        # The index list of the cluster.
        self.indices = indices
        # The Mapping configuration of the cluster.
        self.mapping = mapping
        # The Settings of the cluster.
        self.settings = settings
        # Specifies the type of the index.
        self.type_name = type_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fields is not None:
            result['fields'] = self.fields

        if self.indices is not None:
            result['indices'] = self.indices

        if self.mapping is not None:
            result['mapping'] = self.mapping

        if self.settings is not None:
            result['settings'] = self.settings

        if self.type_name is not None:
            result['typeName'] = self.type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fields') is not None:
            self.fields = m.get('fields')

        if m.get('indices') is not None:
            self.indices = m.get('indices')

        if m.get('mapping') is not None:
            self.mapping = m.get('mapping')

        if m.get('settings') is not None:
            self.settings = m.get('settings')

        if m.get('typeName') is not None:
            self.type_name = m.get('typeName')

        return self

