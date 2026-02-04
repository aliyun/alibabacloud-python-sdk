# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class CreateSlrAndSlsProjectResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sls_info: main_models.CreateSlrAndSlsProjectResponseBodySlsInfo = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about Log Service.
        self.sls_info = sls_info

    def validate(self):
        if self.sls_info:
            self.sls_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sls_info is not None:
            result['SlsInfo'] = self.sls_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SlsInfo') is not None:
            temp_model = main_models.CreateSlrAndSlsProjectResponseBodySlsInfo()
            self.sls_info = temp_model.from_map(m.get('SlsInfo'))

        return self

class CreateSlrAndSlsProjectResponseBodySlsInfo(DaraModel):
    def __init__(
        self,
        end_point: str = None,
        log_store: str = None,
        project: str = None,
        region: str = None,
    ):
        # The endpoint of Log Service.
        self.end_point = end_point
        # The Logstore of Log Service.
        self.log_store = log_store
        # The project of Log Service.
        self.project = project
        # The region where Log Service resides.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_point is not None:
            result['EndPoint'] = self.end_point

        if self.log_store is not None:
            result['LogStore'] = self.log_store

        if self.project is not None:
            result['Project'] = self.project

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')

        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

