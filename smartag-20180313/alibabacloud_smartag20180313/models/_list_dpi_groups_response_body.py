# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class ListDpiGroupsResponseBody(DaraModel):
    def __init__(
        self,
        dpi_group: List[main_models.ListDpiGroupsResponseBodyDpiGroup] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the application group.
        self.dpi_group = dpi_group
        # The token returned for the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.dpi_group:
            for v1 in self.dpi_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DpiGroup'] = []
        if self.dpi_group is not None:
            for k1 in self.dpi_group:
                result['DpiGroup'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dpi_group = []
        if m.get('DpiGroup') is not None:
            for k1 in m.get('DpiGroup'):
                temp_model = main_models.ListDpiGroupsResponseBodyDpiGroup()
                self.dpi_group.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDpiGroupsResponseBodyDpiGroup(DaraModel):
    def __init__(
        self,
        dpi_group_id: str = None,
        dpi_group_name: str = None,
        min_engine_version: str = None,
        min_signature_db_version: str = None,
    ):
        # The ID of the application group.
        self.dpi_group_id = dpi_group_id
        # The name of the application group.
        self.dpi_group_name = dpi_group_name
        # The earliest version of engine that supports the application group.
        self.min_engine_version = min_engine_version
        # The earliest version of signature database that supports the application group.
        self.min_signature_db_version = min_signature_db_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dpi_group_id is not None:
            result['DpiGroupId'] = self.dpi_group_id

        if self.dpi_group_name is not None:
            result['DpiGroupName'] = self.dpi_group_name

        if self.min_engine_version is not None:
            result['MinEngineVersion'] = self.min_engine_version

        if self.min_signature_db_version is not None:
            result['MinSignatureDbVersion'] = self.min_signature_db_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DpiGroupId') is not None:
            self.dpi_group_id = m.get('DpiGroupId')

        if m.get('DpiGroupName') is not None:
            self.dpi_group_name = m.get('DpiGroupName')

        if m.get('MinEngineVersion') is not None:
            self.min_engine_version = m.get('MinEngineVersion')

        if m.get('MinSignatureDbVersion') is not None:
            self.min_signature_db_version = m.get('MinSignatureDbVersion')

        return self

